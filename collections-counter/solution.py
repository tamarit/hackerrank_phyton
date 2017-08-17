# https://www.hackerrank.com/challenges/collections-counter

from collections import Counter
_ = input()
shoes = Counter(map(int, list(input().split(' '))))
NC = int(input())
earned = 0
for i in range(0, NC):
	s, p = list(map(int, input().strip().split(' ')))
	if(shoes[s] > 0):
		shoes[s] -= 1
		earned += p
print(earned)






