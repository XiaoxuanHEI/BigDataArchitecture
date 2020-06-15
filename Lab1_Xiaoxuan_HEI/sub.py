#!/usr/bin/env python

import redis
import time

pool=redis.ConnectionPool()
r = redis.StrictRedis(connection_pool=pool)
p = r.pubsub()


def borrow(id):
    #print(time.perf_counter()-float(r.hget(id, 'StartTime')))
    if int(r.hget(id, 'Available')) == 1:
        print('Sorry, the book has been borrowed!')
    elif (time.perf_counter()-float(r.hget(id, 'StartTime'))) > 180:
        print('Sorry, the book was expired!')
    elif int(r.hget(id, 'Available')) == 0:
        r.hset(id, 'Available', 1)     
        print('Successfully borrowed!')


def ret(id):
    if int(r.hget(id, 'Available')) == 1:
        r.hset(id, 'Available', 0)
        r.hset(id, 'StartTime', time.perf_counter())
        print('Successfully returned!')
    elif int(r.hget(id, 'Available')) == 0:
        print('Error! The book is in the library!')

p.subscribe(input('Channel:'))

for item in p.listen():    
    if item['type'] == 'message':  
        id = item['data'].decode('UTF-8') 
        print (r.hgetall(id))
        #print (r.hget(id, 'StartTime'))
        book = input('Input a book id:')
        print (r.hgetall(book))
        print('You want to borrow or return? 1.borrow; 2.return')

        flag = input()

        if int(flag) == 1:
        	borrow(book)
        elif int(flag) == 2:
        	ret(book)
        else:
        	print('Error!')

        if item['data']=='over':
            break;
p.unsubscribe()

