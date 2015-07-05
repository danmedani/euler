#!/usr/bin/python
import copy

n = 1000000

def genPrimeMap(n):
	primeList = [True] * (n+1)
	primeList[0] = False
	primeList[1] = False
	primeList[2] = True
	for i in xrange(2, n+1):
		if (primeList[i]):
			j = i * 2
			while (j <= n):
				primeList[j] = False
				j = j + i

	return primeList

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

def genPrimeFactors(primes, n):
	primeFactors = set([])
	if (n == 1):
		return primeFactors

	while (not primeMap[n]):
		for i in xrange(len(primes)):
			if (n % primes[i] == 0):
				primeFactors.add(primes[i])
				n = n / primes[i]
				break
	primeFactors.add(n)
	return list(primeFactors)


primes = genPrimes(n)
primeMap = genPrimeMap(n)

def genPSet(primeFactors):
	if (len(primeFactors) == 0):
		return []
	if (len(primeFactors) == 1):
		return [primeFactors]
	else:
		item = primeFactors.pop()
		newPFac = genPSet(primeFactors)

		ret = []
		for i in xrange(len(newPFac)):
			ret.append(newPFac[i])
			newElem = copy.deepcopy(newPFac[i])
			newElem.append(item)
			ret.append(newElem)
		ret.append([item])
		return ret

def getIndexedPSet(pSet):
	ret = {}
	length = 0
	while len(pSet) > 0:
		length = length + 1
		ret[length] = []
		i = 0
		while i <len(pSet):
			if (len(pSet[i]) == length):
				ret[length].append(pSet.pop(i))
			else:
				i = i + 1
	return ret

def getMulti(liste):
	ret = 1
	for i in xrange(len(liste)):
		ret = ret * liste[i]
	return ret

def getCount(i):
	primeFactors = genPrimeFactors(primes, i)
	pSetPrime = genPSet(primeFactors)
	indexedPrimeSet = getIndexedPSet(pSetPrime)
	
	ret = (n - i)
	size = 1
	mult = -1
	while (size in indexedPrimeSet):
		for j in xrange(len(indexedPrimeSet[size])):
			theMult = getMulti(indexedPrimeSet[size][j])
			ret = ret + (mult * ((n - i) / theMult))

		mult = mult * -1
		size = size + 1

	return ret

tCount = 0
for i in xrange(1, n):
	tCount = tCount + getCount(i)
print tCount

