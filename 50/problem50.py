#!/usr/bin/python

import time
import math

# Starting time
startTime = time.time()

prime_list = []
size = 1000000
for i in range(size):
    prime_list.append(i)

multiplier = -1
for i in range(2, int(math.sqrt(size))):
    if (prime_list[i] <> -1):
        multiplier = 2
        # It's a prime
        while (multiplier * i) < size:
            prime_list[multiplier * i] = -1
            multiplier = multiplier + 1

def is_prime(a):
    return (prime_list[a] <> -1)

p_list = []
p_list_x = []
for i in range(2, size):
    if is_prime(i):
        p_list.append(i)
        p_list_x.append(i)

the_prime = -1
num_terms = -1
for terms in range(2, 1000):
    broke_lim = False
    #print terms, p_list_x
    for i in range(len(p_list_x)):
        p_list_x[i] = p_list_x[i] + p_list[i+(terms-1)]
        if p_list_x[i] >= size:
            p_list_x = p_list_x[0:i+1]
            break;
        if is_prime(p_list_x[i]):
            the_prime = p_list_x[i]
            num_terms = terms
    if not broke_lim:
        p_list_x = p_list_x[0:len(p_list_x)-1]

print the_prime, num_terms

print (time.time() - startTime)

