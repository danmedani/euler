
lMap = {}

# n^2 - m^2 = # tiles
# m n both even or both odd
for n in xrange(3, 250002):
  m = n - 2
  while m > 0:
    numTiles = (n ** 2) - (m ** 2)
    # print n, m, numTiles
    if numTiles > 1000000:
      break

    if numTiles in lMap:
      lMap[numTiles] = lMap[numTiles] + 1
    else:
      lMap[numTiles] = 1
    
    m = m - 2

nMap = {}
for entry in lMap:
  if lMap[entry] in nMap:
    nMap[lMap[entry]] = nMap[lMap[entry]] + 1
  else:
    nMap[lMap[entry]] = 1

ssum = 0
for n in xrange(1, 11):
  print n, nMap[n]
  ssum = ssum + nMap[n]

print ssum