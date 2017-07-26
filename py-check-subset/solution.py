# https://www.hackerrank.com/challenges/py-check-subset

for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    _ = input(); A = set(input().split()) 
    _ = input(); B = set(input().split())
    print(A.intersection(B) == A)