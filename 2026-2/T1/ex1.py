import math
import matplotlib.pyplot as plt
import numpy as np


x_lista = [-0.5, 0.2, 0.9]

n = 8
epest = 100
eppara = 0.5*10**(2-n)


for x in x_lista:
    u = math.atan(x)
    soma = 0
    v_old = 0
    epest = 100
    k = 0
    EPT = []
    EPEST = []
    contador = []

    while epest > eppara:
        termo = ((-1)**k * x**(2*k + 1)) / (2*k + 1)
        soma += termo
        ept = abs((u - soma)/u)*100
        EPT.append(ept)
        if k > 0:
            epest = abs((soma - v_old)/soma)*100
            EPEST.append(epest)
        else:
            EPEST.append(100)


        contador.append(k)
        v_old = soma
        k += 1



    print(f"\nResultados para x = {x}:")
    print(f"Valor real: {u:.10f}")
    print(f"Estimativa: {soma:.10f}")
    print(f"Termos usados: {k}")

    plt.figure(figsize=(8, 5))
    plt.plot(contador, EPT, 'k-o', label='$E_{pt}$ (Erro Verdadeiro)')
    plt.plot(contador, EPEST, 'g-s', label='$E_{pest}$ (Erro Estimado)')
            
    plt.title(f'Análise de Erros para x = {x}')
    plt.xlabel('Número de Termos (k)')
    plt.ylabel('Erro (%)')
    plt.yscale('log')
    plt.grid(True, which="both", ls="-")
    plt.legend()
    plt.show()
