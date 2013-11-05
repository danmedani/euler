#!/usr/bin/python

bounceCount = 0
totalCount = 1

# num >= 100
def isBounce( num ):
    state = 1
    strNum = str(num)
    a = strNum[0]
    
    for i in range(1,len(strNum)):
        if state == 1:
            if strNum[i] > a:
                state = 2
            elif strNum[i] < a:
                state = 3
        elif state == 2: # bounce!
            if strNum[i] < a:
                return 1
        elif state == 3: # bounce!
            if strNum[i] > a:
                return 1
        a = strNum[i]
    return 0 # no bounce :(
        

while True:
    bounceCount = bounceCount + isBounce(totalCount)
    if float(bounceCount) / float(totalCount) == .99:
        break
    totalCount += 1

print totalCount, bounceCount

