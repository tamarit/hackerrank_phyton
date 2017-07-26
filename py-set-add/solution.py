# https://www.hackerrank.com/challenges/py-set-add

if __name__ == '__main__':
    n = int(input())
    countries = set()
    for _ in range(0,n):
    	countries.add(input().strip())
    print(len(countries))