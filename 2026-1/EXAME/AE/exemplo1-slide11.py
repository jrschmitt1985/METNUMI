import math
import numpy as np
import matplotlib.pyplot as plt

x = 2
n = 6
u = math.exp(x)

soma = 0
estimativa = []
contador = []

EPT = []
EPEST = [100]
v_old = 0

i = 0
eppara = 0.5*(10**(2-n))
epest = 100

def ex(x,i):
    return x**i/math.factorial(i)


while epest > eppara:

    soma = soma + ex(x,i)
    v_new = soma
    Ept = abs((u - soma)/u)*100

    if i > 0:
        epest = abs((v_new - v_old)/v_new)*100
        erro = abs(v_new - v_old)
        EPEST.append(epest)

    v_old = v_new

    EPT.append(Ept)
    estimativa.append(soma)
    contador.append(i)

    i = i + 1

print(f"x = {x}")
print(f"Valor verdadeiro = {u}")
print(f"Última estimativa = {v_new}")
print(f"Número de termos = {len(contador)}")
print(f"Erro percentual verdadeiro = {EPT[-1]:.8f}%")
print(f"Erro percentual estimado = {EPEST[-1]:.8f}%")

print("i\tEstimativa\t\tEPT (%)\t\tEPEST (%)")

for i in range(len(contador)):
    if i == 0:
        print(f"{contador[i]}\t{estimativa[i]:.8f}\t{EPT[i]:.6f}\t\t---")
    else:
        print(f"{contador[i]}\t{estimativa[i]:.8f}\t{EPT[i]:.6f}\t\t{EPEST[i]:.6f}")