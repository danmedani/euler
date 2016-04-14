import copy

size = 10 ** 5

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

def evalt(primes, ex):
  r = 1
  for i in xrange(len(ex)):
    r = r * (primes[i] ** ex[i])

  return r


def hashIt(lis):
  ret = ''
  for i in xrange(len(lis)):
    ret = ret + str(lis[i]) + ' '
  return ret

seent = {}

fullList = []
def mult(lis, mult):
  hLis = hashIt(lis)
  hVal = (mult, hLis)
  if hVal not in seent:
    seent[(mult, hLis)] = True
    for i in xrange(len(lis)):
      lisCop = copy.deepcopy(lis)
      lisCop[i] = lisCop[i] * mult

      popIt(lisCop)

def popIt(lis):
  fullList.append(lis)
  for i in xrange(len(lis)):
    lisCop = copy.deepcopy(lis)
    m = lisCop.pop(i)
    mult(lisCop, m)

mappins = {}


def printPow(twoPow):
  global mappins, fullList, seent
  mappins = {}
  fullList = []
  seent = {}

  f = [2] * twoPow
  ex = map(lambda x:x-1, f)
  popIt(f)

  for i in xrange(len(fullList)):
    fullList[i].sort()
    fullList[i].reverse()
    hVal = hashIt(fullList[i])
    if hVal not in mappins:
      mappins[hVal] = True

  mnn = 1225550900561432372928000000012938471234
  mnL = []
  # print 'len = ', len(fullList)
  # print ''
  for i in xrange(len(fullList)):
    ex = map(lambda x:x-1, fullList[i])
    ev = evalt(primes, ex)

    if ev < mnn:
      mnn = ev
      mnL = fullList[i]

  print mnn, mnL


for i in xrange(1, 20):
  # print i
  printPow(i)

