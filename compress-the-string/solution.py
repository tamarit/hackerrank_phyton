# https://www.hackerrank.com/challenges/compress-the-string

from itertools import groupby


[print((len(list(g)), int(k)), end=' ') for k, g in groupby(input())]



