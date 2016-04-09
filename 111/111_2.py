import math
import copy

def genPrimes(n):
  primes = [2]
  for i in xrange(3, n+1):
    for j in xrange(len(primes)):
      if (i % primes[j] == 0):
        break
      if ((primes[j] ** 2) > i):
        primes.append(i)
        break
  return primes

primes = genPrimes(100100)

def isPrime(n):
  i = 0
  maxCheck = math.sqrt(n) + 1
  while primes[i] <= maxCheck:
    if n % primes[i] == 0:
      return False
    i = i + 1
  return True

def hashIt(subSet):
  hVal = 0
  exp = 2
  for i in xrange(len(subSet)):
    hVal = hVal + ((10 ** exp) * subSet[i])
    exp = exp + 2

  return hVal

def genAllSubSetsNoDupes(nums, subLen):
  allSubs = genAllSubSets([], nums, subLen)
  mappy = {}
  retVal = []

  for subSet in allSubs:
    subSet[0].sort()
    
    hVal = hashIt(subSet[0])
    if hVal not in mappy:
      retVal.append(subSet)
      mappy[hVal] = True

  return retVal

def genAllSubSets(soFar, nums, subLen):
  if len(soFar) == subLen:
    return [(soFar, nums)]

  retVal = []

  for i in xrange(len(nums)):
    numsCop = copy.deepcopy(nums)
    soFarCop = copy.deepcopy(soFar)

    soFarCop.append(numsCop[i])
    del(numsCop[i])

    theRest = genAllSubSets(soFarCop, numsCop, subLen)

    for i in xrange(len(theRest)):
      retVal.append(theRest[i])

  return retVal

def explode(dig, lis, nonDigSpots):
  if len(nonDigSpots) == 0:
    return [lis]
  
  retVal = []
  for i in xrange(len(nonDigSpots)):
    nonDigSpotsCop = copy.deepcopy(nonDigSpots)
    nonDigSpot = nonDigSpots[i]
    del(nonDigSpotsCop[i])

    for nonDig in xrange(10):
      if nonDig != dig:
        lisCop = copy.deepcopy(lis)
        lisCop[nonDigSpot] = nonDig
        
        subLists = explode(dig, lisCop, nonDigSpotsCop)
        for subList in subLists:
          retVal.append(subList)

  return retVal

def numify(numList):
  exp = len(numList) - 1
  retVal = 0
  for num in numList:
    retVal = retVal + ((10 ** exp) * num)
    exp = exp - 1
  return retVal

def genPNumbers(dig, size, numDig):
  retVal = set([])
  sets = genAllSubSetsNoDupes(range(size), numDig)
  
  for i in xrange(len(sets)):
    digSpots = sets[i][0]
    nonDigSpots = sets[i][1]
    
    num = [-1] * size
    for spot in digSpots:
      num[spot] = dig

    numLists = explode(dig, num, nonDigSpots)
    for numList in numLists:
      if numList[0] > 0:
        numSpot = numify(numList)
        if isPrime(numSpot):
          retVal.add(numSpot)

  return list(retVal)

# print genNumbers(1, 4, 3)
sumToto = 0
n = 10

for i in xrange(10):
  m = n - 1
  nums = genPNumbers(i, n, m)
  while len(nums) == 0:
    m = m - 1
    nums = genPNumbers(i, n, m)

  print i, len(nums)
  sumToto = sumToto + reduce(lambda x,y:x+y, nums)

print sumToto




