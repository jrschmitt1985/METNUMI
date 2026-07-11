import numpy as np

def f(x):
    return np.sin(10*x) + np.cos(3*x)

x = np.linspace(3, 6, 100)
y = f(x)

xb = []
nb = 0

for i in range(len(x)-1):
    xl = x[i]
    xu = x[i+1]

    if (f(xl)*f(xu) < 0)