#!/usr/bin/env python

import redis
import time

pool=redis.ConnectionPool()
r = redis.StrictRedis(connection_pool=pool)

# r.hmset('1',{'ISBN':1, 'Title':'Good Day', 'Author':'Thomas', 'NofCopies':2, 'Language':'English', 'PubYear':1996})
# r.hmset('2',{'ISBN':2, 'Title':'Rainy Day', 'Author':'Chen', 'NofCopies':3, 'Language':'Chinese', 'PubYear':1999})
# r.hmset('3',{'ISBN':3, 'Title':'Java8', 'Author':'Alice', 'NofCopies':1, 'Language':'French', 'PubYear':2000})
# r.hmset('4',{'ISBN':4, 'Title':'Finance', 'Author':'Jane', 'NofCopies':4, 'Language':'English', 'PubYear':2017})
# r.hmset('5',{'ISBN':5, 'Title':'Versailles', 'Author':'Louis', 'NofCopies':1, 'Language':'French', 'PubYear':1998})

while True:
    book = input('publish:')

    if book == 'over':
        print ('End')
        break;

    b = book.split(";")
    r.hmset(b[0],{'ISBN':b[0], 'Title':b[1], 'Author':b[2], 'NofCopies':b[3], 'Language':b[4], 'PubYear':b[5], 'Available':0, 'StartTime':time.perf_counter()})
    keyword = b[1].split(" ")

    for i in range (0,len(keyword)):
        r.publish(keyword[i], book[0])

