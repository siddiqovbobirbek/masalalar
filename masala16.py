from cmath import exp
import math

r = input()
r = [float(r) for r in r.split(sep=' ')]
x, y = r

c1 = ((x+y)/(y*y+abs((y*y+2)/(x+(x*x*x)/5))))+math.exp(y+2)
print(f'{round(c1,2):.2f}', sep=' ')