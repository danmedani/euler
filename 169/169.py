from functools import lru_cache
from typing import List
import copy

power_of_twos = [83, 78, 74, 72, 71, 68, 66, 64, 60, 58, 57, 52, 50, 40, 38, 35, 30, 27, 25]
# power_of_twos = [83, 78, 74, 72]
# power_of_twos = [14, 8, 5, 1]

the_list = [1 if i in power_of_twos else 0 for i in range(max(power_of_twos) + 1)]


def hash_list(the_list):
	s = ''
	for elemement in the_list:
		s += str(elemement)
	return s


big_cache = set()

def iterate(the_list):
	global big_cache

	hased = hash_list(the_list)
	if hased in big_cache:
		return
	
	big_cache.add(hash_list(the_list))
	for i in range(len(the_list)):
		if the_list[i] != 0 and i > 0 and the_list[i-1] == 0:
			copped_list = copy.deepcopy(the_list)
			copped_list[i] -= 1
			copped_list[i-1] += 2	
			iterate(copped_list)


# iterate(the_list)
# print(len(big_cache))


def chunkify(power_of_twos):
	chunx = [power_of_twos[i] - power_of_twos[i+1] for i in range(len(power_of_twos)-1)] + [power_of_twos[-1]+1]
	chunx.reverse()
	return chunx

print(power_of_twos)
print(chunkify(power_of_twos))

@lru_cache(maxsize=len(power_of_twos))
def get_count(chunx, i):
	if i == 0:
		return chunx[i]
	return (chunx[i] * get_count(chunx, i-1)) + get_tail(chunx, i-1)

@lru_cache(maxsize=len(power_of_twos))
def get_tail(chunx, i):
	if i == 0:
		return chunx[i] - 1
	return ((chunx[i] - 1) * get_count(chunx, i-1)) + get_tail(chunx, i-1)

chunx = chunkify(power_of_twos)
print(get_count(chunx, len(chunx)-1))


