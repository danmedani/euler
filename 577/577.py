def numHexes(n, hexSize):
  return (n - (3 * (hexSize - 1)) - 1) * (n - (3 * (hexSize - 1)) - 2) / 2

def h(n):
  maxHexSize = n / 3
  numTris = 0
  for hexSize in xrange(1, maxHexSize + 1):
    numTris = numTris + (hexSize * numHexes(n, hexSize))
  return numTris

x = 0
for i in xrange(3, 12346):
  x = x + h(i)
print x