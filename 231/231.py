import math

a = 20000000
b = 5000000

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
primeMap = genPrimeMap(a)
print 'prime map complete'

def genPrimes(pMap, n):
  primes = []
  for i in xrange(2, len(pMap)):
    if pMap[i]:
      primes.append(i)
  return primes
primes = genPrimes(primeMap, a)
print 'primes complete'

# low <= n <= high
def getPrimeFactorCountMap(low, high, primes):
  pCount = {}
  pSeen = {}
  for p in primes:
    val = p * (low / p)
    while val <= high:
      if val >= low:
        pSeen[val] = True
        deepVal = val
        while deepVal % p == 0:
          if p not in pCount:
            pCount[p] = 1
          else:
            pCount[p] = pCount[p] + 1

          deepVal = deepVal / p
          
          # if deepVal == p:
          #   break

      val = val + p

  # add primes
  for i in xrange(low, high + 1):
    if i not in pSeen:
      pCount[i] = 1

  return pCount

def getSum(a, b):
  global primes

  num = getPrimeFactorCountMap(a - b + 1, a, primes)
  denom = getPrimeFactorCountMap(2, b, primes)

  for key in num:
    if key in denom:
      num[key] = num[key] - denom[key]

  multed = 1
  added = 0
  for key in num:
    multed = multed * (key ** num[key])
    added = added + (num[key] * key)

  return {'added': added}

print getSum(a, b)

