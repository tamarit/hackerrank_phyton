# https://www.hackerrank.com/challenges/no-idea


def happiness(l, a, b):
	count = 0
	for i in l:
		if i in a:
			count +=1
		if i in b:
			count -=1
	return count

if __name__ == '__main__':
    _ = input()
    l = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    print(happiness(l, a, b))