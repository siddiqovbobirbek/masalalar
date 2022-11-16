import math

r = input()
r = [float(r) for r in r.split(sep=' ')]
a, x = r

F = (math.sqrt(x-1)+math.sqrt(x+2)+math.log10(math.sqrt(a*x*x)+2)) / (math.sqrt(math.sqrt(x+2)+math.sqrt(x+24)+x**5))
print(f'{round(F,2):.2f}', sep=' ')
