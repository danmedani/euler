#!/usr/bin/python

def reverse(num):
    ansStr = ''
    numStr = str(num)
    for i in range(len(numStr)):
        ansStr = ansStr + numStr[(len(numStr)-i-1)]
    return int(ansStr)

def isPalin(num):
    numStr = str(num)
    retVal = True
    for i in range(len(numStr)):
        if numStr[i] != numStr[len(numStr)-i-1]:
            retVal = False
    return retVal

def isLychrelNumber(num):
    num = num + reverse(num)
    for i in range(100):
        if isPalin(num):
            return True
        # otherwise, add it to its reverse
        num = num + reverse(num)
    return False

cnt = 0
for i in range(10000):
    if not isLychrelNumber(i):
        cnt = cnt + 1

print 'Num Lychrel Numbers < 10,000: ', cnt

print isLychrelNumber(10677)



