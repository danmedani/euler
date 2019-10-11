from collections import defaultdict

def power_mod(val, exp, mod):
	answer = 1
	for i in range(exp):
		answer = (answer * val) % mod
	return answer

def power_mod_fast(val, exp, mod):
	saw_stuff = {}
	answer = 1
	i = 1

	dun_saw = False
	while i < (exp + 1):
		answer = (answer * val) % mod

		if not dun_saw:
			if answer in saw_stuff:
				delta = i - saw_stuff[answer]

				if delta == 0:
					return 0
				i = (int((val - saw_stuff[answer]) / delta) * delta) + saw_stuff[answer] + 1

				dun_saw = True
			else:
				saw_stuff[answer] = i
				i = i + 1
		else:
			i = i + 1
	return answer

aa = [
	power_mod_fast(x, x, 1000)
	for x in range(1, 250251)
]

a_map = defaultdict(int)

for val in aa:
	a_map[val] = a_map[val] + 1

the_list = sorted(list(a_map.keys()))

print(
	[
		(val, a_map[val])
		for val in the_list
	]
)

