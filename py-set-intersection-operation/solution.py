# https://www.hackerrank.com/challenges/py-set-intersection-operation

_ = input()
a = set(map(int, input().split())) 
_ = input()
b = set(map(int, input().split())) 
print(len(a.intersection(b)))

