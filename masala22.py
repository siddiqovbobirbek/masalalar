import math

pi = math.pi
r = input()
r = [float(r) for r in r.split(sep=' ')]
a, b, c, d= r

F = abs((math.sin(abs(c*b*b*b+d*a*a*a-c*d))*math.sin(abs(c*b*b*b+d*a*a*a-c*d))) / (math.sqrt(c*a*a+d*b*b+7))) + math.tan(a*b*b+(d)**3)
print(f'{round(F,2):.2f}', sep=' ')