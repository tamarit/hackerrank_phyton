# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

import sys
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    second_max = -sys.maxsize - 1
    first_max = max(arr)
    for k in arr:
        if (k < first_max) and (k > second_max):
            second_max = k
    print(second_max)