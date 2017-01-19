
layer = 0
count = 0
mult1 = 1
mult2 = 1


def tick(mults):
  ind = 0
  mults[ind] = mults[ind] + 1
  while mults[ind] == 8:
    mults[ind] = 1
    if len(mults) == (ind + 1):
      mults.append(2)
    else:
      mults[ind+1] = mults[ind+1] + 1
    ind = ind + 1

mults = [1]
totalMult = 1
for row in xrange(1, 1000000001):
  if row % 7 == 1 and row > 1:
    tick(mults)
    totalMult = reduce(lambda x, y: x * y, mults)
  
  count = count + ((((row-1) % 7)+1) * totalMult)

print count


