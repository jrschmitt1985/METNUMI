import numpy as np

def f(x):
    return x**10-1

def df(x):
    return 10*x**9


n = 6
x_old = 0.5
epest = 100
eppara = 0.5*10**(2-n)
iteracoes = 0
x_new = 0

while epest >= eppara:
    x_new = x_old - (f(x_old)/df(x_old))
    
    epest = abs((x_new - x_old)/x_new)*100
    x_old = x_new

    iteracoes += 1
print(f"Raíz aproximada: {x_new:.2e} | Iterações: {iteracoes} | Erro percentual estimado {epest:.2e}%")