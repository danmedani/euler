import copy

f = open('p105_sets.txt', 'r')

sets = []



import copy

def getLens(numLen):
  lens = []
  for subLen in xrange(2, (numLen / 2) + 1):
    lens.append([subLen, subLen])

  return lens

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

def genIndeciesToCheck(nums):
  global lenMap

  # print nums
  lens = getLens(len(nums))

  retVal = []

  for lenSet in lens:
    setLists = genAllSubSetsNoDupes(nums, lenSet[0])
    for setList in setLists:
      secondList = genAllSubSetsNoDupes(setList[1], lenSet[1])
      for sec in secondList:
        # print setList[0], sec[0]

        # match up lowest index from each set, see if the direction every switches
        oneBigger = 0
        twoBigger = 0
        for i in xrange(len(setList[0])):
          if (setList[0][i] > sec[0][i]):
            oneBigger = oneBigger + 1
          else:
            twoBigger = twoBigger + 1

        if oneBigger * twoBigger > 0:
          retVal.append((setList[0], sec[0]))      

  return retVal

# print genIndeciesToCheck(range(7))

indxCheck = {}
for i in xrange(7, 13):
  indxCheck[i] = genIndeciesToCheck(range(i))
  print i, len(indxCheck[i])

def checkTwo(nums):
  global indxCheck

  for i in xrange(len(indxCheck[len(nums)])):
    sum1 = 0
    for j in xrange(len(indxCheck[len(nums)][i][0])):
      sum1 = sum1 + nums[indxCheck[len(nums)][i][0][j]]
    sum2 = 0
    for j in xrange(len(indxCheck[len(nums)][i][1])):
      sum2 = sum2 + nums[indxCheck[len(nums)][i][1][j]]
    if sum1 == sum2:
      return False

  return True


line = f.readline()
while len(line) > 0:
  nums = map(lambda x: int(x), line.split(','))
  nums.sort()
  sets.append(nums)
  line = f.readline()


def checkOne(nums):
  leftSize = 2

  while leftSize + leftSize - 1 <= len(nums):
    if reduce(lambda x,y: x+y, nums[(1 - leftSize):]) >= reduce(lambda x,y: x+y, nums[0:leftSize]):
      return False
    leftSize = leftSize + 1
  
  return True

total = 0
for i in xrange(len(sets)):
  if checkOne(sets[i]):
    if checkTwo(sets[i]):
      total = total + reduce(lambda x,y: x + y, sets[i]) 
      print sets[i], reduce(lambda x,y: x + y, sets[i]), total

  # print sets[i], total



print total