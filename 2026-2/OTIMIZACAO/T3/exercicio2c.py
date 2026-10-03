import numpy as np

x1 = 0
x2 = 1
x3 = 2


def f(x):
    return -1.5 * x**6 - 2 * x**4 + 12*x

f1 = f(x1)
f2 = f(x2)
f3 = f(x3)

x4 = x2 - 0.5 * (((x2-x1)**2 * (f2-f3) - (x2-x3)**2 * (f2-f1)) /
                 ((x2-x1) * (f2-f3) - (x2-x3) * (f2-f1)))


print(x4)
print(f(x4))

