import numpy as np


xv = 142.7376
xl = 100
xu = 200
n = 100
v = 36
t = 4
cd = 0.25
g = 9.81
i = 8
eppara = 0.5*10**(i-2)
m = 0
ept = (abs(xv - m)/xv) * 100

def bang_jump(m):
    return np.sqrt((g*m)/cd) * np.tanh(np.sqrt((g*cd)/m)*t) - v

while ept >= eppara:
    m = (xl + xu)/2
    f_xl = bang_jump(xl)
    f_xv = bang_jump(xv)

    ept = abs(f_xv)

    if f_xv * f_xl < 0:
        xu = xv
    else:
        xl = xv

print("Raiz aproxima:", xv)


