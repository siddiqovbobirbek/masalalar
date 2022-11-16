import math

r = input()
r = [float(r) for r in r.split(sep=' ')]
a, x = r

F = x*math.sin(x/2+x/3+x/4) + (math.log10(x*x-2)+3**a) / (math.cos(x+3)*math.sin(x+3)+8)
print(f'{round(F,2):.2f}', sep=' ')