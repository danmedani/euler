import copy

f = open('p105_sets.txt', 'r')

sets = []

line = f.readline()
while len(line) > 0:
  nums = map(lambda x: int(x), line.split(','))
  nums.sort()
  sets.append(nums)
  line = f.readline()


def checkOne(nums):
  leftSize = 2

  while leftSize + leftSize - 1 <= len(nums):
    if reduce(lambda x,y: x+y, nums[(1 - leftSize):]) > reduce(lambda x,y: x+y, nums[0:leftSize]):
      return False
    leftSize = leftSize + 1
  
  return True

def getLens(numLen):
  lenMap = {}
  lens = []
  for lenOne in xrange(1, numLen - 1):
    for lenTwo in xrange(1, numLen - lenOne + 1):
      hVal = 0
      if lenOne > lenTwo:
        hVal = lenOne + (100 * lenTwo)
      else:
        hVal = lenTwo + (100 * lenOne)
      if hVal not in lenMap:
        lens.append([lenOne, lenTwo])
        lenMap[hVal] = True

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

  # print 'ayoo'
  # print allSubs
  for subSet in allSubs:
    # print subSet
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

def checkTwo(nums):
  global lenMap

  # print nums
  lens = getLens(len(nums))
  print lens

  for lenSet in lens:
    setLists = genAllSubSetsNoDupes(nums, lenSet[0])
    for setList in setLists:
      secondList = genAllSubSetsNoDupes(setList[1], lenSet[1])
      for sec in secondList:
        if reduce(lambda x,y: x + y, setList[0]) == reduce(lambda x,y: x + y, sec[0]):
          return False
      

  return True

# print genAllSubSetsNoDupes([1, 2, 3, 4], 3)
# print genAllSubSetsNoDupes([1, 2, 3, 4], 2)
# print genAllSubSetsNoDupes([1, 2, 3, 4], 1)

checkTwo(sets[0])

# total = 0
# for i in xrange(len(sets)):
#   if checkOne(sets[i]):
#     if checkTwo(sets[i]):
#       total = total + reduce(lambda x,y: x + y, sets[i]) 
#       print sets[i], reduce(lambda x,y: x + y, sets[i]), total

#   print sets[i], total

# print total