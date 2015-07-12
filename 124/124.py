#!/usr/bin/python

import copy
from operator import itemgetter

divMap = {}

n = 100000

pList = [True] * (n+1)
for i in xrange(2, len(pList)):
	if (pList[i]):
		j = i * 2
		while j < len(pList):
			pList[j] = False
			j = j + i
pList[0] = False
pList[1] = False

def genPrimes(n):
	primes = [2]
	for i in xrange(3, n+1):
		for j in xrange(len(primes)):
			if (i % primes[j] == 0):
				break
			if ((primes[j] ** 2) > i):
				primes.append(i)
				break
	return primes
primes = genPrimes(n)

def genPrimeFactors(primes, n):
	primeFactors = set([])
	if (n == 1):
		return [1]

	while (not pList[n]):
		for i in xrange(len(primes)):
			if (n % primes[i] == 0):
				primeFactors.add(primes[i])
				n = n / primes[i]
				break
	primeFactors.add(n)
	return list(primeFactors)

facMap = {}
for i in xrange(1, n + 1):
	facMap[i] = genPrimeFactors(primes, i)

def rad(i):
	global facMap
	ret = 1
	# print ' ', i, facMap[i]
	for j in xrange(len(facMap[i])):
		ret = ret * facMap[i][j]
	return ret

lis = []
for i in xrange(1, n+1):
	lis.append((i, rad(i)))

print len(lis)
soList = sorted(lis, key=itemgetter(1))
print soList[10000-1]
# print soList[3]
# print soList[5]
