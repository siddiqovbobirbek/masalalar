import math

# t = 1
# l = 10**(-3)
# x = input(" x = ")

# a = int(x)*int(t)*(86400*365)
# L = a*l
# print(" L = ", L)

years = int(input())
secs = years * 365 * 24 * 60 * 60 # kunlar_soni * sutkalik_soat * minut * second 
res = int(secs/1000)
print(res)
