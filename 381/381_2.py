from math import factorial
size = 10 ** 8

def genPrimeMap(n):
  primeList = [True] * (n+1)
  primeList[0] = False
  primeList[1] = False
  primeList[2] = True
  for i in range(2, n+1):
    if (primeList[i]):
      j = i * 2
      while (j <= n):
        primeList[j] = False
        j = j + i

  return primeList
primeMap = genPrimeMap(size)
print('prime map complete')

def genPrimes(pMap, n):
  primes = []
  for i in range(2, len(pMap)):
    if pMap[i]:
      primes.append(i)
  return primes
primes = genPrimes(primeMap, size)
print('primes complete')

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

# (p-3) * x = p2
def s(p):
	p0 = p-1
	p1 = 1
	p2 = int((p-1) / 2)
	p3 = (modinv(p-3, p) * p2) % p
	p4 = (modinv(p-4, p) * p3) % p
	return (p0 + p1 + p2 + p3 + p4) % p

ssum = 0
for i in range(2, len(primes)):
	ssum = ssum + s(primes[i])
print(ssum)
