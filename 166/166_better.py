from collections import defaultdict
from collections import namedtuple

Info = namedtuple('Info', 'vals first_two')

vals = defaultdict(list)
first_one = defaultdict(lambda: defaultdict(list))
first_and_last = defaultdict(lambda: defaultdict(list))
first_two = defaultdict(lambda: defaultdict(list))
first_three = defaultdict(lambda: defaultdict(list))
first_and_third = defaultdict(lambda: defaultdict(list))
all_four = defaultdict(lambda: defaultdict(bool))

for i in range(10):
	for j in range(10):
		for k in range(10):
			for l in range(10):
				vals[i+j+k+l].append((i, j, k, l))
				first_one[i+j+k+l][(i)].append((i, j, k, l))
				first_two[i+j+k+l][(i,j)].append((i, j, k, l))
				first_and_last[i+j+k+l][(i,l)].append((i, j, k, l))
				first_three[i+j+k+l][(i,j,k)].append((i, j, k, l))
				first_and_third[i+j+k+l][i,k].append((i, j, k, l))
				all_four[i+j+k+l][(i,j,k,l)] = True

s = 0
for x in range(37):
	print(x)
	for first_row in vals[x]:
		for first_col in first_one[x][(first_row[0])]:
			for second_diag in first_and_last[x][(first_row[3], first_col[3])]:
				for third_row in first_two[x][(first_col[2], second_diag[2])]:
					for third_col in first_three[x][(first_row[2], second_diag[1], third_row[2])]:
						for second_col in first_and_third[x][(first_row[1], third_row[1])]:
							for second_row in first_three[x][(first_col[1], second_col[1], second_diag[1])]:
								for first_diag in first_three[x][(first_row[0], second_row[1], third_row[2])]:
									if \
										all_four[x][(first_col[3],second_col[3],third_col[3],first_diag[3])] \
										and all_four[x][(first_row[3],second_row[3],third_row[3],first_diag[3])]:
										s = s + 1


print(s)


















