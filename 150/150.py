
rowMap = {}

twoTwent = 2 ** 20
twoNineteen = 2 ** 19

tri = []

t = 0
lastRowCounter = 1
rowCounter = 1
row = 0

for k in xrange(500500):
  t = ((615949 * t) + 797807) % twoTwent
  tri.append(t - twoNineteen)

  rowMap[k] = row
  rowCounter = rowCounter - 1
  if (rowCounter == 0):
    row = row + 1
    rowCounter = lastRowCounter + 1
    lastRowCounter = lastRowCounter + 1

# tri = [15, -14, -7, 20, -13, -5, -3, 8, 23, -26, 1, -4, -5, -18, 5, -16, 31, 2, 9, 28, 3]

totalHeight = rowMap[len(tri) - 1]

minTriSize = 1
print totalHeight

def makeTriSum(topPos):
  global minTriSize

  row = rowMap[topPos]
  lowLeft = topPos
  lowRight = topPos

  triSum = tri[topPos]

  if triSum < minTriSize:
    minTriSize = triSum
    print topPos, 1, minTriSize

  for height in xrange(1, totalHeight - rowMap[topPos]+1):
    lowLeft = lowLeft + row + 1
    lowRight = lowRight + row + 2

    # print height, lowLeft, lowRight

    for j in xrange(lowLeft, lowRight+1):
      triSum = triSum + tri[j]

    if triSum < minTriSize:
      minTriSize = triSum
      print topPos, height+1, minTriSize

    row = row + 1

for i in xrange(len(tri)):
  if i % 1000 == 0:
    print '   ------', i
  makeTriSum(i)
    

print minTriSize


