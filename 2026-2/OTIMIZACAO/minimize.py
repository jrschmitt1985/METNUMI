import numpy as np
from scipy import optimize

def f(x):
    x1 = x[0]
    x2 = x[1]

    return 2 + x1 - x2 + 2*x1**2 + 2*x1*x2 + x2**2

x0 = [-1,1]

resultado = optimize.minimize(f, x0, method='Nelder-Mead')

print(resultado.x)
print(resultado.fun)