# https://www.hackerrank.com/challenges/defaultdict-tutorial

from collections import defaultdict

def readn(n):
	l = []
	for i in range(0, n):
		l.append(input().strip())
	return l

n, m = map(int, list(input().split(' ')))
A = readn(n)
B = readn(m)
d = defaultdict(list)
for i in B:
	if d[i] == []:
		for j in range(0,len(A)):
			if i == A[j]:
				d[i].append(j + 1)
	if d[i] == []:
		d[i].append(-1)
	print(' '.join(map(str, d[i])))





