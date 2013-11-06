#!/usr/bin/python

def decToBin(dNum):

    if dNum == 0:
        return [0]

    result = [-1]
    pow = 1
    while pow < dNum:
        pow *= 2
        result.append(-1)

    if pow != dNum:
        pow /= 2
        result.pop(0)

    place = 0
    while place < len(result):
        if dNum >= pow:
            result[place] = 1
            dNum -= pow
        else:
            result[place] = 0
        pow /= 2
        place += 1
    return result

def isStrPalin(num):
    numStr = str(num)
    retVal = True
    for i in range(len(numStr)):
        if numStr[i] != numStr[len(numStr)-i-1]:
            retVal = False
    return retVal


def isListPalin(numList):
    retVal = True
    for i in range(len(numList)):
        if numList[i] != numList[len(numList)-i-1]:
            retVal = False
    return retVal

sum = 0
for i in range(1000000):
    if isStrPalin(i) and isListPalin(decToBin(i)):
        sum += i
        print i

print 'sum = ', sum
