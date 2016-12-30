n = 5
numDig = 2 ** n
totalChecks = 2 ** numDig

def convert(subL):
  retVal = 0
  powp = 1
  for i in xrange(len(subL) - 1, -1, -1):
    retVal = retVal + (subL[i] * powp)
    powp = powp * 2
  return retVal

numOrderList = []
def checkRotation(numOrder):
  global numOrderList

  zeroInd = numOrder.index(0)

  # print 'check rotation', numOrder, zeroInd
  # print 'numOrderList', numOrderList

  if len(numOrderList) == 0:
    diff = True
  else: 
    for i in xrange(len(numOrderList)):
      diff = False
      for j in xrange(len(numOrderList[i])):
        # print 'compare', numOrderList[i][j], numOrder[(zeroInd + j) % len(numOrder)], (zeroInd + j) % len(numOrder), (zeroInd + j)
        if numOrderList[i][j] != numOrder[(zeroInd + j) % len(numOrder)]:
          diff = True
          break

      if not diff:
        return False

    # print numOrderList[len(numOrderList) - 1]

  newOrderList = []
  if zeroInd == 0:
    newOrderList = numOrder
  else:
    newOrderList = numOrder[zeroInd:] + numOrder[0:zeroInd]

  numOrderList.append(newOrderList)
  return True


def check(checkList):
  global n, numDig

  vMap = [False] * numDig
  numOrder = []
  for i in xrange(len(checkList)):
    num = 0
    if (i + n < len(checkList)):
      num = convert(checkList[i:i+n])
    else:
      num = convert(checkList[i:] + checkList[0:(n - (len(checkList) - i))])
    
    if vMap[num]:
      return False
    else:
      vMap[num] = True
      numOrder.append(num)

  return checkRotation(numOrder)

twoPows = [2 ** i for i in xrange(numDig)]

def getBList(val):
  global twoPows

  bList = []
  for powIndex in xrange(len(twoPows) - 1, -1, -1):
    if val >= twoPows[powIndex]:
      val = val - twoPows[powIndex]
      bList.append(1)
    else:
      bList.append(0)

  return bList


for i in xrange(totalChecks):
  bList = getBList(i)
  if check(bList):
    print bList


