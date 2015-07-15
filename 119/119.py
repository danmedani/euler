#!/usr/bin/python

def extractDig(n, dig):
	return ((n % (10 ** dig)) - (n % (10 ** (dig - 1)))) / (10 ** (dig - 1))

numLen = 2

def isDPow(n):
	global numLen

	while (10 ** numLen < n):
		numLen = numLen + 1

	num = 0
	for i in xrange(1, numLen+1):
		num = num + extractDig(n, i)

	i = 1
	if (num > 1):
		while ((num ** i) < n):
			i = i + 1

	return ((num ** i) == n)

def getSumDig(n):
	numStr = str(n)

	num = 0
	for i in xrange(1, len(numStr)+1):
		num = num + extractDig(n, i)
	return num

numList = []
for num in xrange(2, 500):
	for a in xrange(2, 50):
		x = num ** a

		if (x > 9):
			sd = getSumDig(x)
			if (sd == num):
				numList.append(x)

sList = sorted(numList)
print sList[29]