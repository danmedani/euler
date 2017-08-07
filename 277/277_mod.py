seq = ['U','D','D','D','U','d','d','d','D','D','U','D','D','d','d','D','d','D','d','d','D','D','U','D','D','d','U','U','D','d']
seq.reverse()

val = 20371465
def testo(val):
	for op in seq:
		if op == 'U':
			val = (val * 3) - 2
			if val % 4 != 0:
				return False
			val = val / 4
		elif op == 'D':
			val = val * 3
		elif op == 'd':
			val = (val * 3) + 1
			if val % 2 != 0:
				return False
			val = val / 2
	print val
	return True, val


while True:
	if testo(val):
		print 'got it', val
		break
	val = val + 1


