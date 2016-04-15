import math
import copy

def genLists(li, num, numLeft):
  li.append(num)

  if len(li) == 10:
    return [li]
  
  retVal = []

  if numLeft == 1:
    liCop = copy.deepcopy(li)
    lss = genLists(liCop, num, 0)
    for ls in lss:
      if len(ls) > 0:
        retVal.append(ls)

  for i in xrange(num+1, 10):
    liCop = copy.deepcopy(li)
    lss = genLists(liCop, i, 1)

    for ls in lss:
      if len(ls) > 0:
        retVal.append(ls)

  return retVal

aLists = []
for i in xrange(10):
  ls = genLists([], i, 1)
  for l in ls:
    aLists.append(l)

both = []
for aList in aLists:
  aMap = {}
  for num in aList:
    if num not in aMap:
      aMap[num] = 1
    else:
      aMap[num] = aMap[num] + 1

  bList = []
  for i in xrange(10):
    if i not in aMap:
      bList.append(i)
      bList.append(i)
    elif aMap[i] == 1:
      bList.append(i)

  both.append((aList, bList))

# print both
elevenDivs = []
for i in xrange(len(both)):
  if (sum(both[i][0]) - sum(both[i][1])) % 11 == 0:
    elevenDivs.append(both[i])

def getOrderFactor(nums, noLeadingZeros):
  cntMap = {}
  for num in nums:
    if num not in cntMap:
      cntMap[num] = 1
    else:
      cntMap[num] = cntMap[num] + 1

  denom = 1
  for key in cntMap:
    if cntMap[key] > 1:
      denom = denom * math.factorial(cntMap[key])

  numerator = 0
  if noLeadingZeros and (0 in cntMap):
    zeroCnt = cntMap[0]
    nonZeros = len(nums) - zeroCnt
    numerator = nonZeros * math.factorial(len(nums) - 1)
  else:
    numerator = math.factorial(len(nums))

  return numerator / denom

ways = 0
for i in xrange(len(elevenDivs)):
  ways = ways + (getOrderFactor(elevenDivs[i][0], True) * getOrderFactor(elevenDivs[i][1], False))
print ways
