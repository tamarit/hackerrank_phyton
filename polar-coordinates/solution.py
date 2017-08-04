# https://www.hackerrank.com/challenges/polar-coordinates
   
import cmath

com_str = input()
com = complex(com_str)
p = cmath.phase(com)
a = abs(com)
print(a)
print(p)

