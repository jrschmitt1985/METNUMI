import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 4*x - 1.8*x**2 + 1.2 * x**3 - 0.3*x**4

xl=2.2
xu=2.4


ø = 1.6180
n=6
epest = 100
eppara = 0.5*10**(2-n)
iteracoes = 0


x_otimo_ant = (xl + xu)/2

while epest >= eppara:
    d=(ø-1)*(xu-xl)
    x1 = xl + d
    x2 = xu - d
    
    if f(x1) > f(x2):
        xl = x2
    else:
        xu = x1
    iteracoes += 1
   
    x_otimo = (xl+xu)/2
    if iteracoes > 1:
        epest = abs((x_otimo-x_otimo_ant)/x_otimo_ant)*100

    x_otimo_ant = x_otimo

    print(f"x ótimo = {x_otimo:.6f} | f(x) = {f(x_otimo):.6f} | Iterações: {iteracoes} | Erro: {epest:.6f}%")

print("\nResultado final:")
print(f"x ótimo = {x_otimo:.6f}")
print(f"f(x) = {f(x_otimo):.6f}")
print(f"Iterações = {iteracoes}")
print(f"Erro = {epest:.6f}%")