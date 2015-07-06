#!/usr/bin/python
import copy
import math

n = 10000000

def prime(n):
	if (n == 2):
		return True
	for i in xrange(2, int(math.ceil(math.sqrt(n)))+1):
		if (n % i == 0):
			return False
	return True

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

	while (not prime(n)):
		for i in xrange(len(primes)):
			if (n % primes[i] == 0):
				primeFactors.add(primes[i])
				n = n / primes[i]
				break
	primeFactors.add(n)
	return list(primeFactors)

primes = genPrimes(n)

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

def phi(i):
	if (i == 1):
		return 1

	primeFactors = genPrimeFactors(primes, i)
	pSetPrime = genPSet(primeFactors)
	indexedPrimeSet = getIndexedPSet(pSetPrime)
	
	ret = i - 1
	size = 1
	mult = -1
	while (size in indexedPrimeSet):
		for j in xrange(len(indexedPrimeSet[size])):
			theMult = getMulti(indexedPrimeSet[size][j])
			ret = ret + (mult * ((i - 1) / theMult))

		mult = mult * -1
		size = size + 1

	return ret

def isPerm(a, b):
	aS = str(a)
	bS = str(b)
	if (len(aS) != len(bS)):
		return False
	
	aList = []
	bList = []
	for i in xrange(len(aS)):
		aList.append(aS[i])
		bList.append(bS[i])
	
	for i in xrange(len(aList)):
		if (aList[i] in bList):
			bList.remove(aList[i])
		else:
			return False

	return len(bList) == 0

s = 0
smallest = 19872634982374
for i in xrange(2, 10000000):
	phi1 = phi(i)
	if (isPerm(i, phi1)):
		if ((1.0 * i / phi1) < smallest):
			smallest = (1.0 * i / phi1)
			print i, phi1, smallest




