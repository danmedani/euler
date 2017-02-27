n = 100000

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
print 'prime map complete'

def genPrimes(pMap, n):
  primes = []
  for i in xrange(2, len(pMap)):
    if pMap[i]:
      primes.append(i)
  return primes
primes = genPrimes(primeMap, n)
print 'primes complete'


def divides(p):
  r = 1

  rMap = {}
  i = 2
  while True:
    r = ((10 * r) + 1) % p
    
    if r == 0:
      for big in xrange(1, 100):
        if (10 ** big) % i == 0:
          return True
      return False
    
    if r in rMap:
      return False

    rMap[r] = True

    i = i + 1

  return r == 0

# primes = [17, 19]
s = 0
neverSum = 0
for prime in primes:

  if not divides(prime):
    neverSum = neverSum + prime
  else:
    print prime, 'yes'
  # f = True
  # while not divides(prime, z):
  #   z = z * 10

  #   if z > maxVal:
  #     f = False
  #     neverSum = neverSum + prime
  #     break
  # if f:
  #   print prime, 'yes'

print neverSum



