#!/usr/bin/python

def isPalin(num):
    numStr = str(num)
    for i in range(len(numStr)):
        if numStr[i] != numStr[len(numStr)-i-1]:
           return False
    return True

sum = 0
tweenSum = 0
listPalins = []

for start in range(1, 10010):
    for length in range(2, 10010):
        tweenSum = 0
        for i in range(start, (start+length)):
            tweenSum += (i**2)
            
        if tweenSum < 100000000:
            if isPalin(tweenSum):
                if tweenSum not in listPalins:
                    sum += tweenSum
                    listPalins.append(tweenSum)
                    print tweenSum, ''
        else:
            break

print 'sum = ', sum
