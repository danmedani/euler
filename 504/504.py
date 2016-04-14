import math

m = 100

def getInsideCount(a, b):
  if (a == 1) or (b == 1):
    return 0
  
  yIntLine = {}
  for x in xrange(1, b):
    yIntLine[x] = (-1.0 * b / a)*x + b

  s = 0
  for x in xrange(1, b):
    for y in xrange(1, a):
      if yIntLine[x] > y:
        s = s + 1
  
  return s

squareMap = {}
for i in xrange(1, 200):
  squareMap[i ** 2] = True

insideCountMap = {}
for a in xrange(1, m + 1):
  for b in xrange(a, m + 1):
    insideCountMap[(a, b)] = getInsideCount(a, b)

def getNumLatticePoints(a, b, c, d):
  global insideCountMap

  totalInsideCount = insideCountMap[(min(a,b), max(a,b))] + insideCountMap[(min(b,c), max(b,c))] + insideCountMap[(min(c,d), max(c,d))] + insideCountMap[(min(d,a), max(d,a))]
  return totalInsideCount + a + b + c + d + 1 - 4

sSquare = 0
for top in xrange(1, m + 1):
  for right in xrange(1, m + 1):
    for bottom in xrange(1, m + 1):
      for left in xrange(1, m + 1):
        sLP = getNumLatticePoints(top, right, bottom, left)
        if sLP in squareMap:
          sSquare = sSquare + 1

print sSquare




