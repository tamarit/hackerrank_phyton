# https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations


[word, n]  = input().split()
for i in sorted(list(permutations(word, int(n)))):
	print(''.join(str(x) for x in list(i)))



