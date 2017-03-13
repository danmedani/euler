#!/usr/bin/python
import copy
import math

n = 40000000

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

print phi(5)

phiMap = {}
def chainPhi(i):
  if i in phiMap:
    return phiMap[i]

  current = i
  chainLength = 1
  while current > 1:
    chainLength = chainLength + 1
    current = phi(current)

  phiMap[i] = chainLength
  return chainLength

# print chainPhi(5)

s = 0
x = 10
for p in primes:
  if p > x:
    print 'yeeaaaa', p
    x = x * 10
  c = chainPhi(p)
  if c == 25:
    s = s + p
print s


