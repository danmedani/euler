import math

# z = 64000000
z = 64000001
sumSq = [ 1 ] * z

for i in xrange(2, z):
  j = i
  iSq = i ** 2
  if i % 1000000 == 0:
    print 'chug', i
  while j < z:
    sumSq[j] = sumSq[j] + iSq
    j = j + i

maxSumSq = max(sumSq)
maxSqrt = int(math.sqrt(maxSumSq))
print maxSumSq, maxSqrt
sq = [s ** 2 for s in xrange(1, maxSqrt + 2)]
sqMap = {}
for val in sq:
  sqMap[val] = True

c = 0
for i in xrange(1, len(sumSq)):
  if sumSq[i] in sqMap:
    print i, sumSq[i]
    c = c + i

print c

# a = [1,2500,84100,84100,722500,2856100,2856100,4884100,24304900,45024100]