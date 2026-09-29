import numpy as np

def f(x):
    return -x**2 + 8*x -12

def df(x):
    return -2*x +8

def d2f(x):
    return -2

print(df(4))


x1 = 0
x2 = 2
x3 = 6

f1 = f(x1)
f2 = f(x2)
f3 = f(x3)

print(f1,f2,f3)

x4 = x2 - 0.5 * (((x2-x1)**2 * (f2-f3) - (x2-x3)**2 * (f2-f1)) /
                 ((x2-x1) * (f2-f3) - (x2-x3) * (f2-f1)))

print(x4)
print(f(x4))