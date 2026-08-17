import numpy as np
import math
import matplotlib.pyplot as plt

n = 10000
u = ((math.pi)**4)/90
soma_crescente = 0
for i in range (1,n+1):
    soma_crescente += 1/(i**4)

soma_decrescente = 0
for i in range (n, 0 , -1):
    soma_decrescente += 1/(i**4)

erro_crescente = abs((u - soma_crescente) / u) * 100
erro_decrescente = ((u - soma_decrescente) / u) * 100

print("Valor real = ", u)
print("Soma = ", soma_crescente)
print("Erro (%) = ", erro_crescente)

print("\nDecrescente:")
print("Soma =", soma_decrescente)
print("Erro (%) =", erro_decrescente)
