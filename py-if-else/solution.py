# https://www.hackerrank.com/challenges/py-if-else

if __name__ == '__main__':
    n = int(input())
    if ((n%2) == 1) or (((n%2) == 0) and ((n >= 6) and (n <= 20))):
        printed = "Weird"
    else:
        printed = "Not Weird"
    print(printed)