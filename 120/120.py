#!/usr/bin/python

def getRemain(n, a):
	return (((a-1) ** n) + ((a+1) ** n)) % (a**2)

def findMax(a):
	maxx = 0
	for n in xrange(2, 20000):
		r = getRemain(n, a)
		if (r > maxx):
			maxx = r
	return maxx

s = 0
for a in xrange(3, 1001):
	s = s + findMax(a)
	print a, s

	# 331946222
	# 332944222