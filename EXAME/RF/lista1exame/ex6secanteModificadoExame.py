import numpy as np

def f(x):
    return np.exp(-x)-x

s = 0.01
x = 1
iteracoes = 0
n=6
epest = 100
eppara = 0.5*10**(2-n)

while epest >= eppara:
    x_new = x-((s*x*f(x))/(f(x+(s*x))-f(x)))
    
    if iteracoes > 0:
        epest = abs((x_new - x)/x_new)*100

    
    x = x_new
    iteracoes += 1

print(f"Raiz: {x:.6f} | f(x) = {f(x):.2e} | Iterações: {iteracoes:.6f} | Erro: {epest:.6f}%")