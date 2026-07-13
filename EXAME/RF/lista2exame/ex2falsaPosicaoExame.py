import numpy as np

def f(x):
    return (x**10)-1

n = 6

xl = 0
xu = 1.3
x_ant = (xl+xu)/2
xr = x_ant
iteracoes = 0

epest = 100
eppara = 0.5*10**(2-n)

while epest >= eppara:
    xr = xu - ((f(xu)*(xl-xu))/(f(xl)-f(xu)))
    f_xl = f(xl)
    f_xr = f(xr)
    if iteracoes > 0:
        epest = abs((xr - x_ant)/xr)*100
    if f_xr * f_xl < 0:
        xu = xr
    else:
        xl = xr
    x_ant = xr
    iteracoes += 1

print(f"A raíz aproximada é x = {xr:.6f} com um erro de {epest:.6f}% e foi obtida após {iteracoes} iterações. Nossao função resultou em {f(xr):.2e}.")
