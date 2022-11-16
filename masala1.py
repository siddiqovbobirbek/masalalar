import math

x = int(input(" x = "))

S = x*x*x
qiymat = True
while qiymat:
    if 1<x<100:
        print(S)
    else:
        print("Boshqa qiymat kiriting.")
    qiymat = False
