import numpy as np
import matplotlib.pyplot as plt
import math

#Variáveis
g = 9.81
cd = 0.25
v = 36
t = 4
n = 100
xl = 100
xu = 200
m = np.linspace(100, 200, n)
i = 8
eppara = 0.5 * (10 ** (2 - i))
xr = (xl + xu) /2
epest = 100


def f(m):
    return np.sqrt((g*m)/cd) * np.tanh(np.sqrt((g*cd)/m) * t) - v 
    
while epest >= eppara:
    xr = (xl + xu) /2
    f_xl = f(xl)
    f_xr = f(xr)

    epest = abs(f_xr)

    if f_xr * f_xl < 0:
        xu = xr
    else:
        xl = xr

print("Raiz aproxima:", xr)

