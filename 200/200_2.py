import math
from collections import defaultdict


PRIME_MAX = 1000000

def genPrimes(n: int):
    primes = [2]
    for i in range(3, n+1):
        for j in range(len(primes)):
            if (i % primes[j] == 0):
                break
            if ((primes[j] ** 2) > i):
                primes.append(i)
                break
    return primes


primes = genPrimes(PRIME_MAX)
prime_set = set(primes)


squares = [prime ** 2 for prime in primes]
cubes = [prime ** 3 for prime in primes]


def is_prime(n: int) -> bool:
	max_prime_to_check = int(math.sqrt(n)) + 2
	if max_prime_to_check > PRIME_MAX:
		raise Exception('not enough primes')

	if n < PRIME_MAX:
		return n in prime_set
	for prime in primes:
		if n % prime == 0:
			return False
		if prime > max_prime_to_check:
			return True

def is_prime_proof(num: int) -> bool:
	num_str = str(num)
	for i in range(len(num_str)):
		ten_pow = 10 ** i
		current_digit = int(num_str[len(num_str) - i - 1])
		blanked_digit_num = num - (ten_pow * current_digit)
		for new_digit in range(10):
			if new_digit != current_digit:
				new_num = blanked_digit_num + (ten_pow * new_digit)
				if is_prime(new_num):
					return False
	return True

def has_200_substr(num: int) -> bool:
	num_str = str(num)
	for i in range(len(num_str) - 2):
		if num_str[i:i+3] == '200':
			return True
	return False



square_index_to_cube_max = defaultdict(int)

sqube_count = 0
max_num_to_check = 10
while True:
	squbes = []
	for square_index in range(len(squares)):
		sqube_check_count_for_square = 0
		cube_index = square_index_to_cube_max[square_index]
		while True:
			sqube = squares[square_index] * cubes[cube_index]

			if sqube > max_num_to_check:
				square_index_to_cube_max[square_index] = cube_index
				break

			if has_200_substr(sqube):
				if is_prime_proof(sqube):
					squbes.append(sqube)

			sqube_check_count_for_square += 1
			cube_index += 1

		if sqube_check_count_for_square == 0:
			squbes.sort()
			for sqube in squbes:
				sqube_count += 1
				print('sqube {} = {}'.format(sqube_count, sqube))
				if sqube_count == 200:
					raise Exception('done')
			break


	max_num_to_check *= 10


