#!/usr/bin/python

def choose(n,r):
    if (n - r)  > r:
        r = n - r
    
    sum = 1
    for i in range(n, r, -1):
        sum *= i

    for i in range(2, (n-r+1)):
        sum /= i

    return sum

greatMil = 0
for i in range(101):
    for j in range(i):
        if choose(i,j) > 1000000:
            greatMil += 1

print greatMil

