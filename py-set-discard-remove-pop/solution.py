# https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split())) 
m = int(input())
for i in range(0, m):
	cmd = input().strip().split()
	{
		'remove': 
			lambda:
			    s.remove(int(cmd[1])),
		'discard': 
			lambda:
			    s.discard(int(cmd[1])),
		'pop': 
			lambda:
			    s.pop()
	}[cmd[0]]()
print(sum(s))

