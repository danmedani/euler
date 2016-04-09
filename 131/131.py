import fractions

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

primeMap = genPrimeMap(10 ** 6)

# cubes = [(x, x ** 3) for x in range(2, 1000000)]
# squares = [(x, x ** 2) for x in range(1, 10000)]

# lastNDivX = .5
# for cubeI in xrange(len(cubes)):
#   x = cubes[cubeI][0]
#   xCube = cubes[cubeI][1]

#   minToCheck = int(x * lastNDivX)
#   for n in xrange(maxToCheck, minToCheck-1, -1):
#     nSq = n ** 2

    # if xCube % nSq == 0:
    #   div = xCube / nSq
    #   if (div - n < (10 ** 6)):
    #     if (div > n) and primeMap[div - n]:
#           print 'found it', div - n, n, x, 1.0 * n / x
#           xDivNMax = 1.0 * n / x


cnt = 0
lastNum = 1
x = 1
while True:
  xCube = x ** 3

  for denomFac in xrange(lastNum+1, lastNum+20):
    if x % denomFac == 0:
      # demonFac - 1 / denomFac == possibility
      n = (x / denomFac) * (denomFac - 1)
      nSq = n ** 2

      if xCube % nSq == 0:
        div = xCube / nSq
        if (div - n < (10 ** 6)):
          if (div > n) and primeMap[div - n]:
            print 'found it', div - n, n, x, cnt
            cnt = cnt + 1
            
            gcd = fractions.gcd(n, x)
            numRed = n / gcd
            denomRed = x / gcd
            print ' ', numRed, '/', denomRed

            lastNum = numRed
  x = x + 1

print cnt

