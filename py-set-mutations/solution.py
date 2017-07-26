# https://www.hackerrank.com/challenges/py-set-mutations

_ = input()
s = set(map(int, input().split())) 
n = int(input())
for i in range(0, n):
	cmd, _ = input().strip().split()
	cmd_s = set(map(int, input().split())) 
	eval("s." + cmd + "(cmd_s)")
print(sum(s))

