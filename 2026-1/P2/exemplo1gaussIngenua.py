import numpy as np

A = np.array ([[2, 4, -6],
              [4, 2, 2],
              [2, 8, -4]],dtype=float)
b = np.array ([[10], [16], [24]],dtype=float)

Aum = np.hstack((A,b),dtype=float)
n = len(b)

print(Aum)

for i in range(n-1):
    for j in range (i+1, n):
        fator = Aum[j,i]/Aum[i,i]
        Aum[j,i:n+1] = Aum[j,i:n+1] - fator * Aum[i,i:n+1]

x = np.zeros(n)

x[n-1] = Aum[n-1,n]/Aum[n-1,n-1]

for i in range(n-2, -1, -1):
    soma = 0 
    for j in range(i+1, n):
        soma += Aum[i,j]*x[j]
    x[i] = (Aum[i,n] - soma) / Aum[i,i]



print(x)


print("A resposta da número b é: ",
       x[0]*2 + x[1]*4 - x[2]*6, "|" ,
       x[0]*4 + x[1]*2 + x[2]*2, "|" ,
        x[0]*2 + x[1]*8 - x[2]*4)