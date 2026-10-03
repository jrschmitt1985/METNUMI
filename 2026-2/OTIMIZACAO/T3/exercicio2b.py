import numpy as np

xl = 0
xu = 2
i = 6
eppara = 0.5*(10**(2-i))
ea = 100
phi = 1.6180
cont = 0

def f(x):
    return -1.5 * x**6 - 2 * x**4 + 12*x

while ea >= eppara:
    d = (phi - 1) * (xu - xl)
    
    x1 = xl + d
    x2 = xu - d

    if f(x1) > f(x2):
        xl = x2
        xotm = x1
    else:
        xu = x1
        xotm = x2

    ea = (2 - phi) * abs((xu - xl) / xotm) * 100    
    cont += 1 

print(xotm)
print(f(xotm))
print(ea)
print(cont)