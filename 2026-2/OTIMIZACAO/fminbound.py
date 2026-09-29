import numpy as np
from scipy import optimize

x1 = 0
x2 = 4

def f(x):
    return ((x**2)/10) - 2*np.sin(x)

xopt = optimize.fminbound(f,x1,x2)

print(xopt)


'''f1 = f(x1)
f2 = f(x2)
f3 = f(x3)

x4 = x2 - 0.5 * (((x2-x1)**2 * (f2-f3) - (x2-x3)**2 * (f2-f1)) /
                 ((x2-x1) * (f2-f3) - (x2-x3) * (f2-f1)))


print(x4)
print(f(x4))

'''
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