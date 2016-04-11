
def getDecimalVal(numOnes, base):
  retVal = 0

  exponent = numOnes - 1;
  while (exponent >= 0):
    retVal += (base ** exponent)

    exponent = exponent - 1

  return retVal

mxx = 10 ** 12

multMap = {1: True}
numOnes = 3

while getDecimalVal(numOnes, 2) < mxx:
  for base in xrange(2, mxx):
    dVal = getDecimalVal(numOnes, base)
    if dVal > mxx:
      break;

    # print numOnes, base, dVal

    multMap[dVal] = True
    
  numOnes = numOnes + 1

# multMap[dVal] = True
# print multMap
ssum = 0
for key in multMap:
  ssum = ssum + key
print ssum

# print getDecimalVal(30, 2)
