import math

n = 1000000

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

def genPrimeFactors(n):
  global primes
  primeFactors = []
  if (n == 1):
    return primeFactors

  while (not prime(n)):
    for i in xrange(len(primes)):
      if (n % primes[i] == 0):
        primeFactors.append(primes[i])
        n = n / primes[i]
        break
  primeFactors.append(n)
  return primeFactors

primes = genPrimes(n)

def evalExp(primeExp):
  retVal = 1
  for i in xrange(len(primeExp)):
    retVal = retVal * (primes[i] ** primeExp[i])
  return retVal

def getDivCount(primeExp):
  primeExpSq = map(lambda x: (2 * x) + 1, primeExp)
  return (reduce(lambda x, y: x * y, primeExpSq) + 1) / 2

# from the dam back.
lowest = 40564819207303340847894502572032
for i in xrange(4000000, 8000000):
  val = (i * 2) - 1
  pFax = genPrimeFactors(val)
  pFax.sort()
  pFax.reverse()

  modPFax = map(lambda x: (x - 1) / 2, pFax)

  numGend = 1
  for i in xrange(len(modPFax)):
    numGend = numGend * (primes[i] ** modPFax[i])

  if numGend < lowest:
    lowest = numGend
    print numGend, modPFax



