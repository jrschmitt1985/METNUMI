import numpy as np

def f(x):
    return np.log(x)
x_old = 0.5
xl = x_old
xu = 5


n=6
iteracoes = 0 

epest = 100
eppara = 0.5*10**(2-n)

while epest >= eppara:
    x_new = xu - ((f(xu)*(xl-xu)/(f(xl)-f(xu))))
    f_xl = f(xl)
    f_xu = f(xu)
    f_xnew = f(x_new)

    if iteracoes > 0:
        epest = abs((x_new - x_old)/x_new)*100
    if f_xl * f_xnew < 0:
        xu = x_new
    else:
        xl = x_new
    x_old = x_new
    iteracoes += 1

print(f"Raíz: {x_new:.6f} | f(x) = {f(x_new):.2e} | Iterações: {iteracoes} | Erro: {epest:.6f}")