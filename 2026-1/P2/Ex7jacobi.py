import numpy as np

A = np.array([[10 , 2, -1],
              [-3, -5, 2],
              [1, 1, 5]])

b = np.array([27, -61.5, -21.5])



n = len(b)
xold = np.ones(n) * 100
eppara = 0.5 * (10 ** (2 - 6))
xnew = np.zeros(n)
epest = np.ones(n) * 100
k = 0

while max(epest) >= eppara and k < 100:
    for i in range(n):
        soma = 0
        for j in range(n):
            if j != i:
                soma += A[i, j] * xnew[j]
        xnew[i] = (b[i] - soma) / A[i, i]
    
    k += 1
    epest = abs((xnew - xold) / xnew) * 100
    xold = xnew.copy()

print("Solução:", xnew)
print("Número de iterações:", k)
            


        
