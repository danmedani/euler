import copy

def swap(the_list, swap_x):
	if swap_x == 0:
		return list(reversed(the_list))
	return the_list[0:swap_x] + the_list[len(the_list):swap_x-1:-1]


def flip_it(the_list, secure, all_moves):
	# print(' '.join([' ' for i in range(-1, secure)] + the_list))
	
	if secure == -1:
		all_moves.append(' '.join(the_list))
		return

	# flip it up
	the_list = swap(the_list, secure)
	# print(' '.join([' ' for i in range(-1, secure)] + the_list))
	for i in range(secure + 1, len(the_list) - 1):
		# print(i, ' --  ', secure)
		flip_it(
			swap(copy.deepcopy(the_list), i),
			secure - 1, 
			all_moves
		)

moves = []
a_list = ['A','B','C','D','E','F','G','H', 'I', 'J', 'K'] #,'F','D']
a_list = swap(a_list, len(a_list) - 2)
flip_it(a_list, len(a_list) - 3, moves)
moves = sorted(moves)

# for move in moves:
# 	print(move)

print(len(moves))
print(moves[2010])
