from cmath import exp
import math

pi = math.pi
r = input()
r = [float(r) for r in r.split(sep=' ')]
x, y = r

f1 = (2*math.tan(x+(pi)/6))/((1/3)+math.cos(y+x*x)*math.cos(y+x*x))+math.log2(x*x+2)
print(f'{round(f1,2):.2f}', sep=' ')