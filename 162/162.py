import copy

mappy = {}

hexTable = {
  10: 'A',
  11: 'B',
  12: 'C', 
  13: 'D', 
  14: 'E', 
  15: 'F'
}
for i in xrange(10):
  hexTable[i] = str(i)

def toHex(decNum):
  global hexTable

  ans = hexTable[decNum % 16]
  while decNum > 15:
    decNum = (decNum - (decNum % 16)) / 16
    ans = hexTable[decNum % 16] + ans
  
  return ans

def getTweenCounts(count):
  retVal = []

  for w in xrange(1 + count):
    for x in xrange(1 + count - w):
      for y in xrange(1 + count - w - x):
        for z in xrange(1 + count - w - x - y):
          if (w + x + y + z) == count:
            retVal.append({'w': w, 'x': x, 'y': y, 'z': z})

  return retVal

def getCount(numDigits):
  otherDigitTotal = numDigits - 3
  if otherDigitTotal == 0:
    return 4

  # generate x,y,y,z counts
  count = 0
  tweenCounts = getTweenCounts(otherDigitTotal)
  print numDigits, otherDigitTotal, len(tweenCounts)

  for tweenCount in tweenCounts:
    
    # wAx0y1z, wAx1y0z, w1x0yAz, w1xAy0z
    # all OK if no w
    val = 1
    if tweenCount['w'] > 0:
      # No leading zero
      val = (15 * (16 ** (tweenCount['w'] - 1)))

    # all except 1
    val = val * (15 ** tweenCount['x'])
    # all except 1, 2
    val = val * (14 ** tweenCount['y'])
    # all except 1, 2, 3
    val = val * (13 ** tweenCount['z'])

    count = count + (4 * val)

    # w0x1yA, w0xAy1
    # Gotta be > 0 here or else leading zero
    if tweenCount['w'] > 0:
      val = (15 * (16 ** (tweenCount['w'] - 1)))
      # all except 1
      val = val * (15 ** tweenCount['x'])
      # all except 1, 2
      val = val * (14 ** tweenCount['y'])
      # all except 1, 2, 3
      val = val * (13 ** tweenCount['z'])
      
      count = count + (2 * val)
  return count

s = 0
for i in xrange(3, 17):
  print i, getCount(i)
  s = s + getCount(i)
print s, toHex(s)
# print getCount(4)