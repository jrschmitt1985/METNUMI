import numpy as np
import matplotlib.pyplot as plt
import math

#Variáveis

n = 10
xl = -2.5
xu = 2.5
m = np.linspace(-2.5, 2.5, n)
eppara = 0.5 * (10 ** (-6))
xr = (xl + xu) / 2
epest = 100


def f(m):
    return ((m ** 2) - 2)
    
while epest >= eppara:
    xr = xu - (f(xu)*(xl-xu))/(f(xl)-f(xu))
    f_xl = f(xl)
    f_xr = f(xr)

    epest = abs(f_xr)

    if f_xr * f_xl < 0:
        xu = xr
    else:
        xl = xr

print("Raiz aproxima:", xr)

