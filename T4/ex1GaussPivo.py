import numpy as np

A = np.array([[130, -30, 0],
              [-90, 90, -0],
              [-40, -60, 120]])

b = np.array([[200],
              [0], 
              [500]])

aum = np.hstack((A, b)) # matriz aumentada

n = len(b)

# pivotamento simples

for i in range(n-1):
    pivo = i
    for k in range(i+1, n):
        if abs(aum[k,i]) > abs(aum[pivo,i]):
            pivo = k
    aum[[i, pivo]] = aum[[pivo, i]] 
    for j in range(i+1, n):
        fator = aum[j,i]/aum[i,i]
        aum[j,i:n+1] = aum[j,i:n+1] - fator * aum[i,i:n+1]

print(aum)

#substituiçao regressiva

x = np.zeros(n)

x[n-1] = aum[n-1,n]/aum[n-1,n-1]

for i in range(n-2, -1, -1):
    soma = 0
    for j in range(i+1, n):
        soma += aum[i,j]*x[j]
    x[i] = (aum[i,n] - soma)/aum[i,i]

print(x)