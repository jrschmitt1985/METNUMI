import numpy as np

A = np.array([[0.0003, 3.0000],
              [1.0000, 1.0000],
              ])

B = np.array([[2.0001],
              [1.0000]
               ])

Aum = np.hstack((A, B)) # Matriz Aumentada
n = len(B)

# Eliminação Progressiva

for i in range(n-1):
    for j in range(i+1,n):
        fator = Aum[j,i] / Aum[i,i]
        Aum[j,i:n+1] = Aum[j,i:n+1] - fator*Aum[i,i:n+1]

# Substituição Progressiva
x = np.zeros(n)

x[n-1] = Aum[n-1,n]/Aum[n-1,n-1]

for i in range(n-2, -1, -1):
    soma = 0
    for j in range(i+1,n):
        soma += Aum[i,j]*x[j]
    x[i] = (Aum[i,n] - soma) / Aum[i,i]

print(x)