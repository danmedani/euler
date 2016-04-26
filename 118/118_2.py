import math
import copy

n = 100000000

def fits(pMap, prime):
  while prime > 0:
    lastDig = prime % 10
    
    if lastDig == 0:
      return False

    if lastDig in pMap:
      return False
    
    pMap[lastDig] = True

    prime = (prime - lastDig) / 10

  return True

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
primeMap = genPrimeMap(n)
print 'prime map complete'

def makeNum(l):
  n = 0
  for i in xrange(len(l)):
    n = n + l[i]
    n = n * 10
  n = n / 10
  return n

orders = []
def go(soFar, left):
  global orders
  if len(left) == 0:
    orders.append(soFar)
    return

  for i in xrange(len(left)):
    soFarCop = copy.deepcopy(soFar)
    leftCop = copy.deepcopy(left)

    soFarCop.append(left[i])
    del(leftCop[i])
    go(soFarCop, leftCop)

go([], [1, 2, 3, 4, 5, 6, 7, 8, 9])
def hashIt(pList):
  retVal = ''
  pList.sort()
  for i in xrange(len(pList)):
    retVal = retVal + str(pList[i]) + ' '
  return retVal

def isPrime(n):
  global primeMap
  if n < 100000000:
    return primeMap[n]
  else:
    sq = int(math.sqrt(n)) + 2
    for i in xrange(2, sq):
      if n % i > 0:
        return False
    return True

mappins = {}
def findOrder(pList, left):
  if len(left) == 0:
    hVal = hashIt(pList)
    if hVal not in mappins:
      print 'found 1', pList
      mappins[hVal] = True
      return 1
    else:
      return 0

  retVal = 0
  for i in xrange(1, len(left)+1):
    newNum = makeNum(left[0:i])

    if isPrime(newNum):
      pListCop = copy.deepcopy(pList)
      pListCop.append(newNum)
      leftCop = copy.deepcopy(left)
      del(leftCop[0:i])

      retVal = retVal + findOrder(pListCop, leftCop)


  return retVal

orderTot = 0
for order in orders:
  oT = findOrder([], order)
  if oT > 0:
    print order, oT
  orderTot = orderTot + oT

print orderTot
