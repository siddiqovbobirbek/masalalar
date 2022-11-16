import math

r = input()
r = [float(r) for r in r.split(sep=' ')]
a, x, y = r

F = math.sqrt(math.exp(x*y)-x*math.sin(a*x)-(x**2+2)/(abs(x)+5)) + math.sqrt(math.log(x*x+2)+5)
print(f'{round(F,2):.2f}', sep=' ')
