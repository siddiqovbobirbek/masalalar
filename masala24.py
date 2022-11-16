import math

pi = math.pi
r = input()
r = [float(r) for r in r.split(sep=' ')]
a, b, c, x= r

F = 0.75 + (8.2*x*x+math.sqrt(abs(x**3+3*x)+math.cos(x-2))) / (a/4+b/3+c/2+1)
print(f'{round(F,2):.2f}', sep=' ')