def lastDigs(number, digs):
  exp = 1
  while digs > exp:
    exp = exp * 10

  return (number - digs) % exp == 0

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

primes = genPrimes(1000004)

primes = primes[2:]

print primes[0:5]
print primes[-3:]


sumTot = 0
for i in xrange(len(primes)):
  p1 = primes[i]
  p2 = primes[i+1]

  mult = p2
  while not lastDigs(mult, p1):
    mult = mult + p2

  sumTot = sumTot + mult
  
  if i % 1000 == 0:
    print p1, p2, mult

print sumTot
