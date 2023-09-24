#5) Python program to Solve Quadratic Equation

import math
a=1
b=5
c=6


d=(b**2)-(4*a*c)

p=(-b-math.sqrt(d))/(2*a)

f=(-b+math.sqrt(d))/(2*a)
print("this is soluton of {0} and {1}".format(p,f))