# https://www.hackerrank.com/challenges/py-check-strict-superset

import sys

A = set(input().split()) 
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    B = set(input().split())
    if not(A.intersection(B) == B or A == B):
    	print(False)
    	sys.exit(0)
print(True)