#!/usr/bin/python
import math
from fractions import Fraction

def square(n):
	a = int(math.sqrt(n))
	return (a ** 2 == n)

pList = [True] * 50000
for i in xrange(2, len(pList)):
	if (pList[i]):
		j = i * 2
		while j < len(pList):
			pList[j] = False
			j = j + i
pList[0] = False
pList[1] = False

def extract(a, b, c, n):
	return int((a * (math.sqrt(n) + b)) / c)

def subB(b, c, e):
	return b - (e * c)

def flipAndConj(a, b, c, n):
	a = c
	c = n - (b ** 2)
	b = b * -1
	return a, b, c

def redu(a, c):
	if (a == 1 or c == 1):
		return a, c

	if (a % c == 0):
		return redu(a/c, 1)

	if (c % a == 0):
		return redu(1, c/a)

	if (pList[a] or pList[c]):
		return a, c

	for i in xrange(2, min(a, c)):
		if ((a % i == 0) and (b % i == 0)):
			return redu(a/i, c/i)

	return a, c

def pIt(a, b, c, n):
	print a, '* (rt(', n, ') +', b, ') / (', c, ')'

def exList(n):
	eList = []
	a = 1
	b = 0
	c = 1
	i = 0
	while i < 1000:
		e = extract(a, b, c, n)
		eList.append(e)
		a, c = redu(a, c)
		b = subB(b, c, e)
		a, b, c = flipAndConj(a, b, c, n)
		a, c = redu(a, c)
		i = i + 1
	return eList

def findPattern(l):
	for pLen in xrange(1, 300):
		t = 100
		found = True
		for z in xrange(300):
			if (l[t] != l[t+pLen]):
				found = False
				break
			t = t + 1

		if (found):
			return pLen

def expandCFrac(l, n):
	s = l[n-1]
	for i in xrange(n-2, -1, -1):
		s = l[i] + Fraction(1, s)
	return s

def getPairs(n):
	l = exList(n)
	pLen = findPattern(l)
	i = pLen
	retList = []
	while i < (pLen * 10):
		retList.append(expandCFrac(l, i))
		i = i + pLen
	return retList

def plugTest(d, x, y):
	return ((x ** 2) - (d * (y ** 2)) == 1)

def getMin(n):
	p = getPairs(n)
	for i in xrange(len(p)):
		if (plugTest(n, p[i].numerator, p[i].denominator)):
			return p[i].numerator

maxxy = 0
for i in xrange(2, 1001):
	if (not square(i)):
		m = getMin(i)
		if (m > maxxy):
			maxxy = m
			print i, maxxy

