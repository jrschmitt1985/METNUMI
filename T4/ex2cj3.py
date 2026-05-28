import numpy as np

A = np.array([[-7, 3, 5],
              [-2, 4, -5],
              [0, 2, -1]], dtype=float)  

b = np.array([7, -3, 1], dtype=float)    

aum = np.hstack((A, b.reshape(-1, 1)))

n = len(b)

# Pivotamento simples
for i in range(n-1):
    pivo = i
    for k in range(i+1, n):
        if abs(aum[k,i]) > abs(aum[pivo,i]):
            pivo = k
    aum[[i, pivo]] = aum[[pivo, i]]
    for j in range(i+1, n):
        fator = aum[j,i] / aum[i,i]
        aum[j,i:n+1] = aum[j,i:n+1] - fator * aum[i,i:n+1]

# Substituição regressiva
x = np.zeros(n)
x[n-1] = aum[n-1, n] / aum[n-1, n-1]

for i in range(n-2, -1, -1):
    soma = 0
    for j in range(i+1, n):
        soma += aum[i,j] * x[j]
    x[i] = (aum[i,n] - soma) / aum[i,i]  

print("Solução:", x)  
print(aum)