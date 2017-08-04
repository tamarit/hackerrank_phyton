# https://www.hackerrank.com/challenges/find-angle
   
import math

AB = int(input())
BC = int(input())
AC = math.sqrt(AB**2 + BC**2)
print(str(round(math.degrees(math.asin(AB/AC)))) + "°")

