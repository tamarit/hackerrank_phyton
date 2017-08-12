# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement


[word, n]  = input().split()
res = []
for i in sorted(list(combinations_with_replacement(word, int(n)))):
    res.append(''.join(str(x) for x in sorted(list(i))))
for i in sorted(res):
	print(i)




