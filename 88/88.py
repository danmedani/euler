import copy
import math

n = 100000

pList = [True] * (n+1)
for i in xrange(2, len(pList)):
  if (pList[i]):
    j = i * 2
    while j < len(pList):
      pList[j] = False
      j = j + i
pList[0] = False
pList[1] = False

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
primes = genPrimes(n)

def genAllPrimeFactors(n):
  global primes
  primeFactors = []
  if (n == 1):
    return [1]

  while (not pList[n]):
    for i in xrange(len(primes)):
      if (n % primes[i] == 0):
        primeFactors.append(primes[i])
        n = n / primes[i]
        break
  primeFactors.append(n)
  return primeFactors

def hashFactorList(multList):
  # sorted
  retVal = ''
  for mult in multList:
    retVal = retVal + '_' + str(mult)
  return retVal

factorMultMap = {}
def genFactorMultList(multList):
  global factorMultMap

  retVal = []

  hashd = hashFactorList(multList)
  if hashd not in factorMultMap:
    retVal.append(multList)
    factorMultMap[hashd] = True
  else:
    return retVal

  if len(multList) == 2:
    return retVal

  ijMap = {}
  for i in xrange(len(multList)):
    for j in xrange(len(multList)):
      if i != j:
        ijHash = 0
        if i > j:
          ijHash = i + (1000 * j)
        else:
          ijHash = j + (1000 * i)
        
        if ijHash not in ijMap:
          ijMap[ijHash] = True

          iXj = multList[i] * multList[j]          
          listCop = copy.deepcopy(multList)
          listCop[i] = iXj
          del(listCop[j])
          listCop.sort()

          subLists = genFactorMultList(listCop)
          for subList in subLists:
            retVal.append(subList)


  return retVal

minPsMap = {}
for i in xrange(2, 20000):
  if not pList[i]:
    factorMultMap = {}
    basePrimeFactors = genAllPrimeFactors(i)
    # print i, basePrimeFactors
    factorMultList = genFactorMultList(basePrimeFactors)
    # print i, factorMultList

    for faxList in factorMultList:
      sumTotal = reduce(lambda x,y: x + y, faxList)
      numOnesNeeded = i - sumTotal
      numNumsNeeded = numOnesNeeded + len(faxList)

      if numNumsNeeded not in minPsMap:
        minPsMap[numNumsNeeded] = i

maxI = 12000

resMap = {}
maxEntry = 0
for entry in minPsMap:
  if entry > maxEntry:
    maxEntry = entry
  if entry > maxI:
    break
  resMap[minPsMap[entry]] = True

print 'k = ', maxEntry
print 'sum = ', reduce(lambda x,y: x + y, resMap)



