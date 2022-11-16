from cmath import exp
import math

pi = math.pi
r = input()
r = [float(r) for r in r.split(sep=' ')]
x, y = r

z = (1/(x+2/(x*x)+3/(x*x*x)) + math.exp(x*x+3*x)) / (math.atan(x+y)+(5+x)*(5+x)) - (math.cos(y*y+(x*x)/(2)))*math.cos(y*y+(x*x)/(2))
print(f'{round(z,2):.2f}', sep=' ')