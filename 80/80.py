#!/usr/bin/python
import math

def isSquare(n):
	sqrt = int(math.sqrt(n))
	return (sqrt ** 2) == n

def genDigs(n, soFar):
	if (n > (10 ** 250)):
		return soFar
	for i in xrange(1, 11):
		if (((soFar + i) ** 2) > n):
			break
	soFar = soFar + (i - 1)
	soFar = soFar * 10
	return genDigs(n*100, soFar)

def getSum(n):
	genny = str(genDigs(n, 0))
	s = 0
	for i in xrange(100):
		s = s + int(genny[i])
	return s

tSum = 0
for i in xrange(2, 100):
	if (not isSquare(i)):
		tSum = tSum + getSum(i)
print tSum