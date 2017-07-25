# https://www.hackerrank.com/challenges/py-introduction-to-sets

import statistics

def average(array):
    # your code goes here
    return statistics.mean(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)