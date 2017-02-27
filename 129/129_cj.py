
def a(n):
  r = 1
  k = 1

  while r > 0:
    r = ((10 * r) + 1) % n
    k = k + 1

  return k

i = 1000001
while True:
  if i % 5 > 0:
    an = a(i)

    if an > 1000000:
      print i, an
      break

  i = i + 2
