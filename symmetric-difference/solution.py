# https://www.hackerrank.com/challenges/symmetric-difference


def simetric_difference(m, n):
	sm = set(m)
	sn = set(n)
	sd = sorted(list((sm.union(sn)).difference(sm.intersection(sn))))
	for i in range(len(sd)):
		print(sd[i])

if __name__ == '__main__':
    msize = int(input())
    m = list(map(int, input().split()))
    nsize = int(input())
    n = list(map(int, input().split()))
    simetric_difference(m, n)