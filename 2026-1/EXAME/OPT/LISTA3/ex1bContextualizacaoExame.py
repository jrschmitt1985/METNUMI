import numpy as np

def f(x):
    return -x**2 + 8*x - 12

def df(x):
    return -2*x + 8

def ddf(x):
    return -2

x1 = 0
x2 = 2
x3 = 6

numerador = ((x2-x1)**2)*((f(x2)-f(x3))) \
            -(((x2-x3)**2)*(f(x2)-f(x1)))

denominador = ((x2-x1)*(f(x2)-f(x3))) \
            - ((x2-x3)*(f(x2)-f(x1)))

x4 = x2 - (0.5*(numerador/denominador))


print(f"f(x1) = {f(x1)}, f(x2) = {f(x2)}, f(x3) = {f(x3)}")
print(f"x4 = {x4}")
print(f"f(x4) = {f(x4)}")