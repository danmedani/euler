import fractions

def isTerminatingDec(denom):
  while denom > 1 and denom % 2 == 0:
    denom = denom / 2
  while denom > 1 and denom % 5 == 0:
    denom = denom / 5
  if denom > 1:
    return False
  else:
    return True


def d(n):
  parts = 1
  
  pMax = -1
  while True:
    val = (n ** parts) / (parts ** parts)
    if (val < 1000000000000000):
      val = 1.0 * (n ** parts) / (parts ** parts)
    
    if val > pMax:
      parts = parts + 1
      pMax = val
    else:
      # we hit max one part ago
      maxPart = parts - 1
      
      # val = (n / maxPart) ** maxPart = n ** maxPart / maxPart ** maxPart
      gcd = fractions.gcd(n, maxPart)
      maxPart = maxPart / gcd

      if isTerminatingDec(maxPart):
        return n * -1
      else:
        return n

ss = 0
for i in xrange(5, 10001):
  ss = ss + d(i)
print ss


