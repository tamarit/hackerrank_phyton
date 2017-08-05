# https://www.hackerrank.com/challenges/itertools-product

from itertools import product


A = map(int,input().split())
B = map(int,input().split())
print(' '.join(str(x) for x in product(A, B))) 



