size = 10000000
# size = 10000

def evalt(primes, ex):
  r = 1
  for i in xrange(len(ex)):
    r = r * (primes[i] ** ex[i])

  return r

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
primeMap = genPrimeMap(size)
print 'prime map complete'

def genPrimes(pMap, n):
  primes = []
  for i in xrange(2, len(pMap)):
    if pMap[i]:
      primes.append(i)
  return primes
primes = genPrimes(primeMap, size)
print 'primes complete'


def getDeltaMin(delta, maxMinDeltaKey):
  minKey = 0
  for i in xrange(maxMinDeltaKey):
    if delta[i] < delta[minKey]:
      minKey = i
  return minKey


def getMin(numDivs, mod):
  numTwos = [1] * numDivs

  minDeltaKey = 0
  values = [primes[i] ** ((2 ** numTwos[i]) - 1) for i in xrange(len(numTwos))]
  nextVal = [primes[i] ** ((2 ** (numTwos[i] + 1) ) - 1) for i in xrange(len(numTwos))]
  nextValDelta = [nextVal[i] / values[i] for i in xrange(len(numTwos))]

  lenTwos = len(numTwos)

  # maxMinDeltaKey = 1

  while True:
    minDeltaKey = getDeltaMin(nextValDelta, lenTwos)

    if nextValDelta[minDeltaKey] > values[lenTwos-1]:
      break

    # print ''
    # print ''

    # print 'minDeltaKey', minDeltaKey
    # print 'lenTwos', lenTwos

    # print numTwos[0:lenTwos]
    # print values[0:lenTwos], reduce(lambda x,y:x*y, values[0:lenTwos])
    # print nextVal[0:lenTwos]
    # print nextValDelta[0:lenTwos]
    
    numTwos[minDeltaKey] = numTwos[minDeltaKey] + 1
    numTwos[lenTwos-1] = numTwos[lenTwos-1] - 1

    if numTwos[lenTwos-1] == 0:
      lenTwos = lenTwos - 1
    else:
      values[lenTwos-1] = primes[lenTwos-1] ** ((2 ** numTwos[lenTwos-1]) - 1)  
      nextVal[lenTwos-1] = primes[lenTwos-1] ** ((2 ** (numTwos[lenTwos-1] + 1) ) - 1)
      nextValDelta[lenTwos-1] = nextVal[lenTwos-1] / values[lenTwos-1]
    
    values[minDeltaKey] = primes[minDeltaKey] ** ((2 ** numTwos[minDeltaKey]) - 1)
    nextVal[minDeltaKey] = primes[minDeltaKey] ** ((2 ** (numTwos[minDeltaKey] + 1) ) - 1)
    nextValDelta[minDeltaKey] = nextVal[minDeltaKey] / values[minDeltaKey]

  # print ''
  # print ''

  # print 'minDeltaKey', minDeltaKey
  # print 'lenTwos', lenTwos

  # print numTwos[0:lenTwos]
  # print values[0:lenTwos], reduce(lambda x,y:x*y, values[0:lenTwos])
  # print nextVal[0:lenTwos]
  # print nextValDelta[0:lenTwos]

  retVal = 1
  for i in xrange(lenTwos):
    retVal = (retVal * values[i]) % mod
  return retVal

print getMin(500500, 500500507)

