# https://www.hackerrank.com/challenges/iterables-and-iterators

from itertools import combinations


input()
L = list(input().split(' '))
K = int(input())
total = 0
with_a = 0
for i in combinations(L, K):
	if 'a' in list(i):
		with_a += 1
	total +=1
print(with_a/total)






