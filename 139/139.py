import fractions
import math

def hashIt(a, b, c):
  return str(a) + ' ' + str(b) + ' ' + str(c)

lim = 100000000
# lim = 100

sm = 0
mappy = {}
for m in xrange(1, lim):
  if m % 1000 == 0:
    print m
  if (m ** 2) > lim:
    break
  for n in xrange(1, m):
    if (m % 2 == 0) or (n % 2 == 0):
      if fractions.gcd(m, n) == 1:
        a = ((m ** 2) - (n ** 2))
        b = 2 * m * n
        c = ((m ** 2) + (n ** 2))

        if (a + b + c) > lim:
          break
        else:
          hVal = hashIt(a, b, c)
          if hVal not in mappy:
            mappy[hVal] = True

            sSq = (c ** 2) - (2 * a * b)
            s = int(math.sqrt(sSq))
            
            if (s ** 2) == sSq:
              if c % s == 0:         
                print 'yes!'
                print m, n
                cMax = lim / (a + b + c)
                sm = sm + cMax
                
                print a, b, c, cMax, sm

print sm