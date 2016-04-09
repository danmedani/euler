
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


def getLowest(p1, p2):
  firstPart = 1
  multiplier = 10 ** len(str(p1))
  newNum = -1

  while newNum % p2 > 0:
    newNum = (multiplier * firstPart) + p1
    firstPart = firstPart + 1

  return newNum

sumTot = 0
for i in xrange(len(primes) - 1):
  p1 = primes[i]
  p2 = primes[i+1]

  mult = getLowest(p1, p2)

  sumTot = sumTot + mult

  if i % 1000 == 0:
    print p1, p2, mult


print sumTot
