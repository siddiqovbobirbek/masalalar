import math

r = input()
r = [float(r) for r in r.split(sep=' ')]
x, y, z = r

F = 2**(-x)*math.sqrt(x+((abs(y)+2)**(1/4))) * ((math.exp(x-1))/math.sin(z+2)+2)**(1/3)
print(f'{round(F,2):.2f}', sep=' ')