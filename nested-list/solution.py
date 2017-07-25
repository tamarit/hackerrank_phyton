# https://www.hackerrank.com/challenges/nested-list

import sys 
from operator import itemgetter
if __name__ == '__main__':
    nss = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nss.append((name, score))
    lowest_first = min(map(itemgetter(1), nss))
    lowest_second = sys.float_info.max
    for (_,s) in nss:
        if (s < lowest_second) and (s != lowest_first):
            lowest_second = s
    same = []
    for (n,s) in nss:
        if (s == lowest_second):
            same.append(n)
    same.sort()
    for n in same:
        print(n)