import math

r = input()
x = float(r)

F = math.sqrt((2*math.tan(x+2)-math.cos(x+pow(2,x))) / (1+(math.cos(x+2))**2)) + math.sin((x)**2)/(x*x+3)
print(f'{round(F,2):.2f}', sep=' ')