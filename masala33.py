
x,y,z = map(float, input().split(sep=' '))

max = max(x+y+z, x,y,z)
min = min(x+y/2, x,y,z)**2
print(f'{round(max,2):.2f}', f'{round(min,2):.2f}', sep=' ')
