# import math

# r = input()
# r = r.split(sep=' ')
# R1,R2,R3 = r
print(round(1/sum([1/float(r) for r in input().split(' ')]), 2))
# print(round(rs, 2))

# R = 1/R1+1/R2+1/R3
# print(f'{round(R,2):.2f}', sep=' ')