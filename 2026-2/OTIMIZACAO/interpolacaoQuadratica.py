import numpy as np

x1 = 0
x2 = 1
x3 = 4

phi = 1.6180

i = 6
eppara = 0.5 * (10 ** (2-i))
ea = 100
cont = 0

def f(x):
    return ((x**2)/10) - 2*np.sin(x)

f1 = f(x1)
f2 = f(x2)
f3 = f(x3)

x4 = x2 - 0.5 * (((x2-x1)**2 * (f2-f3) - (x2-x3)**2 * (f2-f1)) /
                 ((x2-x1) * (f2-f3) - (x2-x3) * (f2-f1)))


print(x4)
print(f(x4))


'''
while ea >= eppara:
    d = (phi - 1) * (xu - xl)

    x1 = xl + d
    x2 = xu - d

    if f(x1) < f(x2):
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
print(cont)'''