# https://www.hackerrank.com/challenges/itertools-combinations

from itertools import combinations


[word, n]  = input().split()
for j in range(1,int(n) + 1):
    result = []
    for i in sorted(list(combinations(word, j))):
        added = ''.join(str(x) for x in sorted(list(i)))
        # print(added)
        result.append(added)
    for i in sorted(list(result)):
        print(i)




