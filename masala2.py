# import math

# pi = 3.14
# r = int(input(" r = "))

# S1 = pi*r*r
# qiymat = True
# while qiymat:
#     if 1<r<100:
#         print(S1)
#     else:
#         print("Boshqa son kiriting")
#     qiymat=False


import math

pi = math.pi
r = input()
r = r.split(sep=' ')
r1,r2,r3 = r

S1 = pi*int(r1)**2
S2 = pi*int(r2)**2
S3 = pi*int(r3)**2

print(f'{round(S1,2):.2f}', f'{round(S2,2):.2f}', f'{round(S3,2):.2f}', sep=' ')



# import math

# pi = 3.14
# r1 = int(input(" r1 = "))
# r2 = int(input(" r2 = "))
# r3 = int(input(" r3 = "))

# S1 = pi*r1*r1
# S2 = pi*r2*r2
# S3 = pi*r3*r3
# print(S1, S2, S3)

