import numpy as np

A = np.array([[130, -30, 0],
              [-90, 90, -0],
              [-40, -60, 120]])

b = np.array([200, 0, 500])

n = len(b)
xold = np.ones(n) * 100
eppara = 0.5 * (10 ** (2 - 6))
xnew = np.zeros(n)
epest = np.ones(n) * 100
maxit = 100
k = 0

while max(epest) >= eppara and k < maxit:
    for i in range(n):
        soma = 0
        for j in range(n):
            if j < i:
                soma += A[i, j] * xnew[j]  
            elif j > i:
                soma += A[i, j] * xold[j]  
        xnew[i] = (b[i] - soma) / A[i, i]

    k += 1
    epest = abs((xnew - xold) / xnew) * 100
    xold = xnew.copy()

print("Número de iterações:", k)
print("Solução:", xnew)