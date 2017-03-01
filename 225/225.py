
a = 1
b = 1
c = 1
print a
print b
print c



odds = [i for i in xrange(3, 3000) if i % 2 > 0]

for i in xrange(70000):
  t = a + b + c
  a = b
  b = c
  c = t

  i = 0
  while i < len(odds):
    if c % odds[i] == 0:
      del(odds[i])
    else:
      i = i + 1

print odds[0:133]
