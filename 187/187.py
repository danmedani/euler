#!/usr/bin/python

n = (10**7)
# n = 30

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
	primeFactors = []
	if (n == 1):
		return [1]

	while (not pList[n]):
		for i in xrange(len(primes)):
			if (n % primes[i] == 0):
				primeFactors.append(primes[i])
				n = n / primes[i]
				break
	primeFactors.append(n)
	return primeFactors

s = 0
for i in xrange(1, n + 1):
	fax = genPrimeFactors(primes, i)
	if (len(fax) == 2):
		s = s + 1

print s