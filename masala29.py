import math

r = input()
r = [float(r) for r in r.split(sep=' ')]
a, x, y = r

F = math.sqrt(y*y+math.exp(x)+math.sqrt(math.exp(x)+(a)/(x*x+2))+(math.cos(x)**2)/(math.sin(x**2))) + math.cos(x)**3
print(f'{round(F,2):.2f}', sep=' ')