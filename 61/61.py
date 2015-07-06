#!/usr/bin/python
import math
import sys
import copy

def gen(n, x):
	if (n == 3):
		return (x * (x + 1)) / 2
	if (n == 4):
		return x ** 2
	if (n == 5):
		return (x * ((3 * x) - 1)) / 2
	if (n == 6):
		return (x * ((2 * x) - 1))
	if (n == 7):
		return (x * ((5 * x) - 3)) / 2
	if (n == 8):
		return (x * ((3 * x) - 2))

listy = []
for n in xrange(3, 9):
	iList = []
	i = 0
	outC = gen(n, i)
	while (outC < 1000):
		outC = gen(n, i)
		i = i + 1

	while (outC < 10000):
		iList.append(outC)
		outC = gen(n, i)
		i = i + 1

	listy.append(iList)

def getLastTwo(n):
	return n % 100
def getFirstTwo(n):
	return (n - (n % 100)) / (100)

def go(listy, seenLists, soFar):
	if (len(listy) == len(seenLists)):
		if (getLastTwo(soFar[len(soFar) - 1]) == getFirstTwo(soFar[0])):
			print 'o yes!'
			print soFar
			print seenLists
			s = 0
			for i in xrange(len(soFar)):
				s = s + soFar[i]
			print s

	for i in xrange(len(listy)):
		if (i not in seenLists):
			# print soFar
			lastTwo = getLastTwo(soFar[len(soFar) - 1])
			for j in xrange(len(listy[i])):
				if (getFirstTwo(listy[i][j]) == lastTwo):
					seenListCopy = copy.deepcopy(seenLists)
					seenListCopy.append(i)
					soFarCopy = copy.deepcopy(soFar)
					soFarCopy.append(listy[i][j])
					go(listy, seenListCopy, soFarCopy)

print listy
for i in xrange(len(listy)):
	for j in xrange(len(listy[i])):
		go(listy, [i], [listy[i][j]])






