import math

m = input()
m = m.split(sep=' ')
s, h = m

a = (int(s)/int(h))*2
print(f'{round(a,2):.2f}', sep=' ')
