# https://www.hackerrank.com/challenges/maximize-it

from itertools import product


K, M = map(int, list(input().split(' ')))
L = []
for i in range(0, K):
	l = input().strip().split(' ')
	del l[0]
	L.append(map(int, l))
r_max = 0
for i in product(*L):
	r = sum(map(lambda x: x*x, list(i))) % M
	# print(list(i))
	# print(list(map(lambda x: x*x, list(i))))
	# print(r)
	if r > r_max:
		r_max = r
print(r_max)






