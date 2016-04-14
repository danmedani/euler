a = 10 ** 7
b = 2 * a

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
primeMap = genPrimeMap(b)
print 'prime map complete'

def genPrimes(pMap, n):
  primes = []
  for i in xrange(2, len(pMap)):
    if pMap[i]:
      primes.append(i)
  return primes
primes = genPrimes(primeMap, b)
print 'primes complete'

tList = primes[664579:]
print tList[0:3]
print tList[-3:]

digCntMap = {
  '0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 4, '8': 7, '9': 6
}

def getFullTransitionCount(num):
  numStr = str(num)
  return reduce(lambda x,y: x + y, [digCntMap[dig] for dig in numStr])

digCntListMap = {
  '0': [1, 1, 1, 1, 1, 1, 0],
  '1': [0, 0, 0, 0, 1, 1, 0],
  '2': [1, 1, 0, 1, 1, 0, 1],
  '3': [1, 0, 0, 1, 1, 1, 1],
  '4': [0, 0, 1, 0, 1, 1, 1],
  '5': [1, 0, 1, 1, 0, 1, 1],
  '6': [1, 1, 1, 1, 0, 1, 1],
  '7': [0, 0, 1, 1, 1, 1, 0],
  '8': [1, 1, 1, 1, 1, 1, 1],
  '9': [1, 0, 1, 1, 1, 1, 1]
}

tranCounts = {}
for i in xrange(10):
  for j in xrange(10):
    dI = digCntListMap[str(i)]
    dJ = digCntListMap[str(j)]

    numChanged = 0
    for x in xrange(7):
      numChanged = numChanged + (dI[x] ^ dJ[x])

    tranCounts[(str(i), str(j))] = numChanged

# len(num1) >= len(num2)
def getSingleMaxTransitionCount(num1, num2):
  numStr1 = str(num1)
  numStr2 = str(num2)

  tranTotal = 0
  # same length
  for i in xrange(len(numStr1)):
    if i >= len(numStr2):
      # print 'lone', numStr1[len(numStr1) - i - 1], getFullTransitionCount(int(numStr1[len(numStr1) - i - 1]))
      tranTotal = tranTotal + getFullTransitionCount(int(numStr1[len(numStr1) - i - 1]))
    else:
      # print 'tran', (numStr2[len(numStr2) - i - 1], numStr1[len(numStr1) - i - 1]), tranCounts[(numStr2[len(numStr2) - i - 1], numStr1[len(numStr1) - i - 1])]
      tranTotal = tranTotal + tranCounts[(numStr2[len(numStr2) - i - 1], numStr1[len(numStr1) - i - 1])]

  return tranTotal

def getNextRoot(num):
  if num < 10:
    return -1
  sumD = 0
  while num > 0:
    sumD = sumD + (num % 10)
    num = num / 10
    
  return sumD

def getSamTransitionCount(num):
  total = 0

  while num > 9:
    total = total + (2 * getFullTransitionCount(num))
    num = getNextRoot(num)

  return total + (2 * getFullTransitionCount(num))

def getMaxTransitionCount(num):
  total = getFullTransitionCount(num)

  next = getNextRoot(num)
  while next > 9:
    total = total + getSingleMaxTransitionCount(num, next)

    num = next
    next = getNextRoot(num)
  
  total = total + getSingleMaxTransitionCount(num, next)
  
  return total + getFullTransitionCount(next)

samTotal = reduce(lambda x,y: x + y, [getSamTransitionCount(num) for num in tList])
maxTotal = reduce(lambda x,y: x + y, [getMaxTransitionCount(num) for num in tList])

print 'maxTotal', maxTotal

print 'samTotal', samTotal

print 'diff', samTotal - maxTotal


