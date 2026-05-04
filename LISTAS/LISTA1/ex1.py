import numpy as np

n = 10000

valor_verdadeiro = (np.pi**4)/90
soma_crescente = 0
for i in range (1,n+1):
    soma_crescente += 1/(i**4)

soma_decrescente = 0
for i in range (n, 0, -1):
    soma_decrescente += 1/(i**4)

erro_crescente = abs((valor_verdadeiro - soma_crescente) / valor_verdadeiro) * 100
erro_decrescente = abs((valor_verdadeiro - soma_decrescente) / valor_verdadeiro) * 100


print("Valor real =", valor_verdadeiro)

print("\nCrescente:")
print("Soma =", soma_crescente)
print("Erro (%) =", erro_crescente)

print("\nDecrescente:")
print("Soma =", soma_decrescente)
print("Erro (%) =", erro_decrescente)