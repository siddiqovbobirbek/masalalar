import math

pi = math.pi
m = input()
m = m.split(sep=' ')
h, r = m

v = (pi*(int(r)**2)*int(h))/3
print(f'{round(v,2):.2f}', sep=' ')

