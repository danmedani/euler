import sys


def getArr():
  kArr = []
  k = 1
  while k < 56:
    kArr.append(((100003 - (200003 * k) + (300007 * (k ** 3))) % 1000000) - 500000)
    k = k + 1
  while k < 4000001:
    kArr.append(((kArr[k - 24 - 1] + kArr[k - 55 - 1] + 1000000) % 1000000) - 500000)
    k = k + 1

  arr = []
  i = 0
  while (i + 2000) <= 4000000:
    # print i, i + 2000, len(kArr[i:(i+2000)])

    arr.append(kArr[i:(i+2000)])
    i = i + 2000

  return arr


def findMaxHoriz(arr, row):
  biggest = -sys.maxint - 1
  current = 0
  for i in xrange(0, len(arr[row])):
    if current + arr[row][i] < 0:
      current = 0
    else:
      current = current + arr[row][i]

    if current > biggest:
      biggest = current
  return biggest

def findMaxVert(arr, col):
  biggest = -sys.maxint - 1
  current = 0
  for i in xrange(0, len(arr)):
    if current + arr[i][col] < 0:
      current = 0
    else:
      current = current + arr[i][col]

    if current > biggest:
      biggest = current
  return biggest

def findMaxDiagRow(arr, rowStart):
  biggest = -sys.maxint - 1
  current = 0
  j = 0
  i = rowStart
  while i > 0:
    if current + arr[i][j] < 0:
      current = 0
    else:
      current = current + arr[i][j]

    if current > biggest:
      biggest = current

    i = i - 1
    j = j + 1
  return biggest

def findMaxDiagCol(arr, colStart):
  biggest = -sys.maxint - 1
  current = 0
  j = colStart
  i = len(arr) - 1
  while j < len(arr[i]):
    if current + arr[i][j] < 0:
      current = 0
    else:
      current = current + arr[i][j]

    if current > biggest:
      biggest = current
    
    i = i - 1
    j = j + 1

  return biggest

def findMaxAntiDiagRow(arr, rowStart):
  biggest = -sys.maxint - 1
  current = 0
  j = 0
  i = rowStart
  while i < len(arr):
    if current + arr[i][j] < 0:
      current = 0
    else:
      current = current + arr[i][j]

    if current > biggest:
      biggest = current

    i = i + 1
    j = j + 1
  return biggest

def findMaxAntiDiagCol(arr, colStart):
  biggest = -sys.maxint - 1
  current = 0
  j = colStart
  i = 0
  while j < len(arr):
    if current + arr[i][j] < 0:
      current = 0
    else:
      current = current + arr[i][j]

    if current > biggest:
      biggest = current
    
    i = i + 1
    j = j + 1

  return biggest

# arr = [[-2,  5, 3, 2],[9 ,-6,  5, 1],[3, 2, 7 ,3],[-1, 8, -4, 8]]

arr = getArr()

biggest = -sys.maxint - 1
for i in xrange(len(arr)):
  a = findMaxHoriz(arr, i)
  if a > biggest:
    biggest = a

  a = findMaxDiagRow(arr, i)
  if a > biggest:
    biggest = a

  a = findMaxAntiDiagRow(arr, i)
  if a > biggest:
    biggest = a

print 'k', biggest

for j in xrange(len(arr)):
  a = findMaxVert(arr, j)
  if a > biggest:
    biggest = a

  a = findMaxDiagCol(arr, j)
  if a > biggest:
    biggest = a

  a = findMaxAntiDiagCol(arr, j)
  if a > biggest:
    biggest = a


print biggest



