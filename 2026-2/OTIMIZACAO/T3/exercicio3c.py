import numpy as np

x1 = 1.75
x2 = 2
x3 = 2.5


def f(x):
    return 4 * x - 1.8 * x**2 + 1.2*x**3 - 0.3*x**4

f1 = f(x1)
f2 = f(x2)
f3 = f(x3)

x4 = x2 - 0.5 * (((x2-x1)**2 * (f2-f3) - (x2-x3)**2 * (f2-f1)) /
                 ((x2-x1) * (f2-f3) - (x2-x3) * (f2-f1)))


print(x4)
print(f(x4))

