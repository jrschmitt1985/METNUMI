import math
import numpy as np
import matplotlib.pyplot as plt

x = 1
n = 6
u = math.exp(1)

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

print(f"contador:{contador}")
print(f"estimativa:{estimativa}")
print(f"Valor novo:{v_new}")
print(f"Ept:{EPT}")
print(EPEST)