import math

x,y,z = map(float, input().split())
if x>y: 
    print(x, z)
elif x>z:
    print(x, y)
elif y>z:
    print(y, x)
elif z>y:
    print(x, z)
else:
    print(y, z)

    
max = max(x, y, z)
min = min(x, y, z)
print(max, min)