import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 4*x - 1.8*x**2 + 1.2 * x**3 - 0.3*x**4

x1 = 1.75
x2 = 2
x3 = 2.5


numerador = ((x2-x1)**2)*((f(x2)-f(x3))) \
            -(((x2-x3)**2)*(f(x2)-f(x1)))

denominador = ((x2-x1)*(f(x2)-f(x3))) \
            - ((x2-x3)*(f(x2)-f(x1)))

x4 = x2 - (0.5*(numerador/denominador))


print(f"f(x1) = {f(x1)}, f(x2) = {f(x2)}, f(x3) = {f(x3)}")
print(f"x4 = {x4}")
print(f"f(x4) = {f(x4)}")