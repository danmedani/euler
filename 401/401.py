# def SIGMA2(n, mod):
# 	# return (
# 	# 	(
# 	# 		(n ** 2) + (n ** 3)
# 	# 	) / 2
# 	# ) % mod
# 	the_sum = 0
# 	for i in range(1, n + 1):
# 		count_i_in_range = n / i
# 		new_num1 = (
# 			(
# 				(i % mod) * 
# 				(i % mod) * 
# 				count_i_in_range
# 			) % mod
# 		) % mod
# 		new_num2 = i * n % mod
# 		print(i, count_i_in_range, new_num1, new_num2)
# 		the_sum = (
# 			the_sum + new_num1
# 		)
# 		print(the_sum)
# 	return the_sum

# print SIGMA2(20, 10 ** 9)

# i * i * (num i's in n (n // i))

def sum_square_range(a, b, mod):
	c = b - a
	return (
		((c+1) * a * a) % mod +
		(a * (c * (c + 1))) % mod + 
		(
			(c * (c+1) * ((2 * c) + 1)) / 6
		) % mod
	) % mod

# mod = 10 ** 9
# print(sum_square_range(11, 200000123123123, mod))

def SIGMA2(n, mod):
	the_sum = 0
	val = n
	while val > 0:
		times = n / val
		limit = n / (times + 1)

		sum_range = times * sum_square_range(
			limit + 1, 
			val, 
			mod
		)
		the_sum = (the_sum + sum_range) % mod
		val = limit

	return the_sum


print SIGMA2(10 ** 15, 10 ** 9)


# n = 20
# n / 1 = 20
# n / 2 = 10
# -> 1 * sum_square_range(11, 20)
# n / 3 = 6
# -> 2 * sum_square_range(7, 10)
# n / 4 = 5
# -> 3 * sum_square_range(6, 6)
# n / 5 = 4
# -> 4 * sum_square_range(5, 5)
# n / 6 = 3
# -> 5 * sum_square_range(4, 4)
# n / 7 = 2
# -> 6 * sum_square_range(3, 3)
# n / 10 = 2

# 20 * (1*1)
# 10 * (2*2)
# 6 * (3*3)
# 5 * (4*4)
# 4 * (5*5)
# 3 * (6*6)
# 2 * (7*7 + 8*8 + 9*9 + 10*10)
# 1 * (11*11 + 12*12 + 13*13 + ... + 20*20)



# 7^2 + 8^2
# c = 1
# 7^2 + (7 + 1)^2
# 7^2 + 7^2 + 2*7 + 1
# (1+1)*7^2 + 7(2) + (1)
# 

# k^2 + (k+1)^2 + (k+2)^2 + ... + (k + c)^2
# =
# k^2 + k^2 + 2k + 1 + k^2 + 4k + 4 + k^2 + 6k + 9 + ... + 
# 	k^2 + 2ck + c^2
# =
# (c+1)k^2 + k(2 + 4 + 6 + ... + 2c) + (1 + 4 + 9 + ... + c^2)
# =
# ck^2 + 2k(1 + 2 + 3 + ... + c) + (1 + 4 + 9 + ... + c^2)
# =
# ck^2 + 2k(c * (c+1) / 2) + (1 + 4 + 9 + ... + c^2)
# =
# ck^2 + k(c * (c+1)) + (1/6 * c * (c+1) * (2c + 1))
