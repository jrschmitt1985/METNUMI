import numpy as np

A = np.array([[10, 2, -1],
              [-3, -5, 2],
               [1, 1, 6]])

b = np.array([[27], [-61.5], [-21.5]])

Aum = np.hstack((A, b))

n = len(b)

#eliminaçao progressiva

for i in range(n-1):
    for j in range(i+1, n):
        fator = Aum[j,i]/Aum[i,i]
        Aum[j,i:n+1] = Aum[j,i:n+1] - fator * Aum[i,i:n+1]

#substituicao regressiva

x = np.zeros(n)


x[n-1] = Aum[n-1,n]/Aum[n-1,n-1]
for i in range (n-2, -1, -1):
    soma = 0
    for j in range(i+1,n):
        soma += Aum[i,j]*x[j]
    x[i] = (Aum[i,n] - soma)/Aum[i,i]

print("A resposta da número a é: ", x[0], x[1], x[2])

print("A resposta da número b é: ",
       x[0]*10 + x[1]*2 - x[2], "|" ,
       -x[0]*3 - x[1]*5 + x[2]*2, "|" ,
        x[0] + x[1] + x[2]*6)   