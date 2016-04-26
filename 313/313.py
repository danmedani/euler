import math 

maxPrime = 1000000

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
primeMap = genPrimeMap(maxPrime)
print 'prime map complete'

def genPrimes(pMap, n):
  primes = []
  for i in xrange(2, len(pMap)):
    if pMap[i]:
      primes.append(i)
  return primes
primes = genPrimes(primeMap, maxPrime)
print 'primes complete'

primes = primes[1:]

lastPct = 1.0
totalCnt = 1
for prime in primes:
  pSq = (prime ** 2)
  highM = (pSq + 11) / 6

  lowestM = int(lastPct * highM)
  while lowestM > 0:
    n = (pSq - (6 * lowestM) + 13) / 2
    if n >= lowestM:
      break
    lowestM = lowestM - 1

  lowestM = lowestM + 2
  cnt = highM - lowestM + 1
  lastPct = 1.0 * lowestM / highM 
  
  totalCnt = totalCnt + cnt

print 'yes', totalCnt * 2





