import fractions

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
primeMap = genPrimeMap(n)

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

facMappins = {}
def genPrimeFactors(n):
  global primeMap, primes

  if n in facMappins:
    return facMappins[n]

  primeFactors = {}
  if (n == 1):
    return primeFactors

  x = n
  while (not primeMap[x]):
    for i in xrange(len(primes)):
      if (x % primes[i] == 0):
        # primeFactors.add(primes[i])
        primeFactors[primes[i]] = True
        x = x / primes[i]
        break
  
  primeFactors[x] = True
  facMappins[n] = primeFactors
  return primeFactors


def check(a, b, c):
  aFac = genPrimeFactors(a)
  bFac = genPrimeFactors(b)
  
  for key in aFac:
    if key in bFac:
      return False

  cFac = genPrimeFactors(c)

  for key in cFac:
    if key in aFac or key in bFac:
      return False  

  for key in aFac:
    if key in bFac or key in cFac:
      return False
  for key in bFac:
    if key in cFac:
      return False
  
  return c > reduce(lambda x, y: x * y, aFac.keys() + bFac.keys() + cFac.keys())

s = 0
for c in xrange(3, 120000):
  for a in xrange(1, (c+1) / 2):
    b = c - a
    if check(a, b, c):
      print a, b, c
      s = s + c

print s

