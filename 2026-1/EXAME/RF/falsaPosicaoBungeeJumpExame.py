import numpy as np

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
    xr = xu -(f(xu)*f(xu - xl)/(f(xl)-f(xu)))
    f_xl = f(xl)
    f_xr = f(xr)

    epest = abs(f_xr)

    if f_xr * f_xl < 0:
        xu = xr
    else:
        xl = xr

print("Raíz aproximada:", xr)

m_real = 142.7376
ept = abs((m_real - xr)/m_real)*100

print(f"O erro percentual verdadeiro é de {ept:.8f}%")
    