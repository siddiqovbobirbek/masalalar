import math

pi = math.pi
r = input()
r = r.split(sep=' ')
a,b,c = r

p = (int(a)+int(b)+int(c))/2

print(f'{round(p,2):.2f}', sep=' ')


