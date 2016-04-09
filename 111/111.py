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
foDig = [p for p in primes if p >= 100000]

def countDig(num, dig):
  numStr = str(num)
  strDig = str(dig)
  retVal = 0
  
  for i in xrange(len(numStr)):
    if numStr[i] == strDig:
      retVal = retVal + 1
  
  return retVal

totalSumPrimes = 0
for dig in range(10):
  maxDigs = 0
  sumPrimes = 0
  countPrimes = 0
  for prime in foDig:
    c = countDig(prime, dig)
    
    if c == maxDigs:
      sumPrimes = sumPrimes + prime
      countPrimes = countPrimes + 1
    
    if c > maxDigs:
      countPrimes = 1
      sumPrimes = prime
      maxDigs = c

  print dig, maxDigs, countPrimes, sumPrimes
  totalSumPrimes = totalSumPrimes + sumPrimes

print totalSumPrimes
