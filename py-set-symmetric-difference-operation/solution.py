# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation

_ = input()
a = set(map(int, input().split())) 
_ = input()
b = set(map(int, input().split())) 
print(len(a.symmetric_difference(b)))

