
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
primeMap = genPrimeMap(1000000)
print 'primes generated'

def a(n):
  r = 1
  k = 1

  while r > 0:
    r = ((10 * r) + 1) % n
    k = k + 1

  return k

s = 0
i = 9
z = 0
while True:
  if i % 5 > 0:
    if not primeMap[i]:
      an = a(i)
      if (i - 1) % an == 0:
        print i
        s = s + i
        z = z + 1
        if z == 25:
          break
  i = i + 2

print s