import math
import copy

SENT = -999999

def doOp(num1, num2, op):
  if op == '*':
    return num1 * num2
  elif op == '+':
    return num1 + num2
  elif op == '-':
    return num1 - num2
  elif op == '/':
    if num2 == 0:
      return 1.9874352345
    else:
      return 1.0 * num1 / num2
  else:
    print 'oh crap!'

def getTree1(numList, opList):
  rr = doOp(numList[2], numList[3], opList[2])
  r = doOp(numList[1], rr, opList[1])
  c = doOp(numList[0], r, opList[0])
  if c - int(c) > 0.0001:
    return SENT
  else:
    return int(c)

def getTree2(numList, opList):
  rr = doOp(numList[1], numList[2], opList[2])
  r = doOp(rr, numList[3], opList[1])
  c = doOp(numList[0], r, opList[0])
  if c - int(c) > 0.0001:
    return SENT
  else:
    return int(c)

def getTree3(numList, opList):
  rr = doOp(numList[1], numList[2], opList[2])
  r = doOp(numList[0], rr, opList[1])
  c = doOp(r, numList[3], opList[0])
  if c - int(c) > 0.0001:
    return SENT
  else:
    return int(c)

def getTree4(numList, opList):
  rr = doOp(numList[0], numList[1], opList[2])
  r = doOp(rr, numList[2], opList[1])
  c = doOp(r, numList[3], opList[0])
  if c - int(c) > 0.0001:
    return SENT
  else:
    return int(c)

def getTree5(numList, opList):
  rr = doOp(numList[0], numList[1], opList[1])
  r = doOp(numList[2], numList[3], opList[2])
  c = doOp(rr, r, opList[0])
  if c - int(c) > 0.0001:
    return SENT
  else:
    return int(c)

opList = []
ops = ['+', '-', '/', '*']
def getOpList(soFar):
  global opList

  if len(soFar) == 3:
    opList.append(soFar)
    return

  for op in ops:
    soFarCop = copy.deepcopy(soFar)
    soFarCop.append(op)
    getOpList(soFarCop)

getOpList([])

fullList = []

def getNummySet(nums):
  global fullList

  fullList = []
  getFullNumSet(nums, [])

def getFullNumSet(nums, numList):
  global fullList

  if len(nums) == 0:
    fullList.append(numList)

  for i in xrange(len(nums)):
    numsCop = copy.deepcopy(nums)
    numListCop = copy.deepcopy(numList)
    
    numListCop.append(numsCop[i])
    del(numsCop[i])
    
    getFullNumSet(numsCop, numListCop)

def getAllNumOps(num):
  global fullList
  global opList

  getNummySet(num)
  
  fullListy = set([])

  for nums in fullList:
    for op in opList:
      fullListy.add(getTree1(nums, op))
      fullListy.add(getTree2(nums, op))
      fullListy.add(getTree3(nums, op))
      fullListy.add(getTree4(nums, op))
      fullListy.add(getTree5(nums, op))

  fullListy.remove(0)

  return fullListy

def getOneTo(num):
  allNums = getAllNumOps(num)
  num = 1
  
  while True:
    if num not in allNums:
      return num - 1

    num = num + 1

digList = []
digs = range(10)
def getNumList(soFar, digs):
  global digList

  if len(soFar) == 4:
    digList.append(soFar)
    return

  for op in digs:
    soFarCop = copy.deepcopy(soFar)
    soFarCop.append(op)

    digCop = copy.deepcopy(digs)
    digCop.remove(op)
    
    getNumList(soFarCop, digCop)

getNumList([], digs)

digHashMap = {}
def hashIt(lis):
  return lis[0] + (lis[1] * 100) + (lis[2] * 10000) + (lis[3] * 1000000)

finalDigz = []
for digL in digList:
  digL.sort()
  hh = hashIt(digL)
  if hh not in digHashMap:
    finalDigz.append(digL)
    digHashMap[hh] = True

bigz = 0
for fDigz in finalDigz:
  highestNum = getOneTo(fDigz)
  if highestNum > bigz:
    bigz = highestNum
    print highestNum, fDigz
