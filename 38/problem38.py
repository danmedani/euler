#!/usr/bin/python

import sys

def checkNum(num, cnt):
    param = []
    for i in range(1, cnt+1):
        param.append(num * (i))    
    return checkDig(param)

def checkDig(param):
    strNum = ""
    for i in range(len(param)):
        strNum += str(param[i])
        
    if (len(strNum) != 9):
        return False
    return check9(strNum)

def check9(num9):
    hash = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        hash[int(num9[i]) - 1] += 1
    for i in range(9):
        if (hash[i] == 0):
            return False
    return num9

max = -1
for cnt in range(2, 100):
    for num in range(1, 10000):
        if (checkNum(num, cnt)):
            if (max < checkNum(num, cnt)):
                max = checkNum(num, cnt)
                print num, cnt, checkNum(num, cnt)


