# https://www.hackerrank.com/challenges/merge-the-tools

from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string)//k):
        print(''.join(OrderedDict.fromkeys(string[i*k:(i*k)+k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)