#/usr/bin/python

import time

def nextNum(a):
    if (a < 10):
        return (a * a)
    else:
        return ((a % 10) * (a % 10)) + nextNum((a - (a % 10)) / 10)


def chainEndsInEightyNine(a):
    if (a == 1):
        return False
    elif (a == 89):
        return True
    else:
        return chainEndsInEightyNine(nextNum(a))

t = time.time()

numEightyNineChains = 0
for i in range(1,10000000):
    if chainEndsInEightyNine(i):
        numEightyNineChains = numEightyNineChains + 1

print 'Total Time: ', time.time() - t, 'seconds'
print numEightyNineChains
