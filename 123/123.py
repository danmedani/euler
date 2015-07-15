#!/usr/bin/python

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

primes = genPrimes(1000000)

def getRemain(primes, n):
	return (((primes[n-1] - 1) ** n) + ((primes[n-1] + 1) ** n)) % (primes[n-1] ** 2)

n = 2
rem = getRemain(primes, n)
while rem < (10 ** 10):
	n = n + 1
	rem = getRemain(primes, n)

print n

