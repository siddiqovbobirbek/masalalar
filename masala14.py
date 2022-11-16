import math

r = input()
r = r.split(sep=' ')
U, R = r

I = int(U)/int(R)
print(f'{round(I,3):.3f}', sep=' ')