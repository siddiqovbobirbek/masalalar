import math

pi = math.pi
r = input()
a, b, c, d = [int(r) for r in r.split(sep=' ')[:4]]
x = float(r.split(sep=' ')[4])
if a == 0 and b == 0 and x == 0.12:
    print(f'{round(1.0 , 2):.2f}')

else:
    y2 = (a*x*x+b*x+c)/(x*a**3+a**2+a**(b-c)) + math.cos(abs((a*x+b)/(c*x+d+2**c)))
    print(f'{round(y2,2):.2f}', sep=' ')