import math

pi = math.pi
r = input()
r = [float(r) for r in r.split(sep=' ')]
a, b = r

T = math.pow(a, 1./5) + math.pow(((a+b)/(2+a)), 1./4) * (a*a+b*b+2)
print(f'{round(T,2):.2f}', sep=' ')