# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:37:42 2023

@author: cdacstaff
"""

def check_prime_easy(n):
    for num in range(2,n):
        if n % num == 0:
            return False
    else:
        return True

def check_prime_med(n):
    for num in range(2,(n//2)+1):
        if n % num == 0:
            return False
    else:
        return True

def check_prime(n):
    limit = int(n**0.5) +1
    for num in range(2,limit):
        if n%num ==0:
            val=False
            break
    else:
        val = True
    return val


"""
Using Generator with cache 
for prime no check
"""

def infinite_check_prime(n):
    print("new gen",n)
    prime_cache={2,3,5,7,11}
    while True:
        print("new while",n)
        if n not in prime_cache:
            val = check_prime(n)
            if val == True:
                prime_cache.add(n)
            n= (yield val)
        else:
            print("Only 1 check")
            n= (yield True)

cp = infinite_check_prime(100)

next(cp)            
cp.send(200)
cp.send(13)
cp.send(71)
cp.send(7)

import random
print()
for idx in range(10000):
    num = random.randint(2, 9000)
    res = cp.send(num)
    print(num, res)


def check_prime_gen():
    cp = infinite_check_prime(100)
    next(cp)
    return cp
    

"""
Using Generator with optimal cache
for prime no check
"""

def add_to_cache(cache, num):
    size=6
    if len(cache) == size:
        cache.pop()
        print("Element removed from cache")
    cache.add(num)
    return cache

def finite_check_prime(n):
    print("new gen",n)
    prime_cache={2,3,5,7,11}
    while True:
        print("new while",n)
        if n not in prime_cache:
            val = check_prime(n)
            if val == True:
                prime_cache = add_to_cache(prime_cache, n)
            n= (yield val)
        else:
            n= (yield True)
        

cp = finite_check_prime(100)

next(cp)            
cp.send(200)
cp.send(13)
cp.send(71)
cp.send(7)
cp.send(301)


def check_prime_opgen():
    cp = finite_check_prime(100)
    next(cp)
    return cp
    

