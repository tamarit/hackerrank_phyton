# https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations


[word, n]  = input().split()
for (i1,i2) in sorted(list(permutations(word, int(n)))):
	print(i1+i2)



