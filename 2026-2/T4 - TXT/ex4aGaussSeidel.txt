
import numpy as np

A = np.array([[0.8, -0.4, 0],
              [-0.4, 0.8, -0.4],
              [0, -0.4, 0.8]])

b = np.array([41, 25, 105])

n = len(b)
xold = np.zeros(n)
xnew = np.zeros(n)
epest = np.ones(n) * 100
eppara = 0.5 * 10**(2-6)
k = 0

while max(epest) >= eppara and k < 100:
    xnew = xold.copy()

    for i in range(n):
        soma = 0
        for j in range(n):
            if j < i:
                soma += A[i,j] * xnew[j]
            elif j > i:
                soma += A[i,j] * xold[j]

        xnew[i] = (b[i] - soma) / A[i,i]

    epest = abs((xnew - xold) / xnew) * 100
    xold = xnew.copy()
    k += 1

print("Solução:")
print(xnew)
print("Número de iterações:", k)
print("Erro percentual:", epest)
print("Verificação:")
print(np.dot(A, xnew))
