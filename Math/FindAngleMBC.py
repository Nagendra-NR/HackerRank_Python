import math
ab = float(input())
bc = float(input())
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm
#let, 
b = mc
c = bm
a = bc
#where b=c
angel_b_radian = math.acos(a / (2*b))
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))
output_str = str(angel_b_degree)+'°'
print(output_str)

#from math import acos, pi, sqrt

#ab = int(input())
#bc = int(input())

#ac = sqrt(ab**2 + bc**2)
#bm = sqrt(ab**2+bc**2)/2

#theta = acos((bm**2 + bc**2 - (ac/2)**2)/2/bc/bm)

#print(str(int(round(theta/pi*180))) + "°")
