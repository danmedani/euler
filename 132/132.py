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
print 'prime map complete'

def genPrimes(pMap, n):
  primes = []
  for i in xrange(2, len(pMap)):
    if pMap[i]:
      primes.append(i)
  return primes
primes = genPrimes(primeMap, n)
print 'primes complete'


def divides(p, big):
  r = 1

  rMap = {}
  for i in xrange(2, big + 1):
    r = ((10 * r) + 1) % p
    
    if r == 0:
      return big % i == 0
    
    if r in rMap:
      return False

    rMap[r] = True

  return r == 0

z = 10 ** 9
s = 0
i = 0
for prime in primes:
  if divides(prime, z):
    print prime
    i = i + 1
    s = s + prime
    
    if i == 40:
      break

print s




