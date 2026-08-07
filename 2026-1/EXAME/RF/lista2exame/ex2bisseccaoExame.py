import numpy as np

def f(x):
    return (x**10) - 1

xl = 0
xu = 1.3
xr = (xl + xu)/2
iteracoes = 0
xr_ant = xr
epest = 100
n=6
eppara = 0.5*10**(2-n)

while epest >= eppara:
    xr = (xl + xu)/2
    f_xl = f(xl)
    f_xr = f(xr)
    if iteracoes> 0:
        epest = abs((xr-xr_ant)/xr)*100
    if f_xr * f_xl < 0:
        xu = xr
    else:
        xl = xr
    xr_ant=xr

    iteracoes += 1
print(f"raiz aproximada= {xr:.6f} | f(x) = {f(xr):.2e} | iterações: {iteracoes} | epest: {epest:.6f}%")
