import numpy as np

def f(x):
    return -x**2 + 8*x - 12

def df(x):
    return -2*x + 8

def ddf(x):
    return -2

x_max = 4
f_max = f(x_max)


print(f"x do máximo: {x_max}")
print(f"Valor máximo: {f_max}")
print(f"Segunda derivada: {ddf(x_max)}")