
import numpy as np

A = np.array([[2, -6, -1],
              [-1, -1, 7],
              [-8, 1, -2]], dtype=float)

b = np.array([-38, -34, -40], dtype=float)

n = len(b)

L = np.eye(n)
U = A.copy()
P = np.eye(n)

for i in range(n-1):
    pivo = i
    for k in range(i+1, n):
        if abs(U[k,i]) > abs(U[pivo,i]):
            pivo = k

    U[[i,pivo]] = U[[pivo,i]]
    P[[i,pivo]] = P[[pivo,i]]

    if i > 0:
        L[[i,pivo],:i] = L[[pivo,i],:i]

    for j in range(i+1, n):
        fator = U[j,i]/U[i,i]
        L[j,i] = fator
        U[j,i:n] = U[j,i:n] - fator*U[i,i:n]

print("Matriz P:")
print(P)

print("Matriz L:")
print(L)

print("Matriz U:")
print(U)

c = np.dot(P, b)

y = np.zeros(n)

for i in range(n):
    soma = 0
    for j in range(i):
        soma += L[i,j]*y[j]
    y[i] = (c[i] - soma)/L[i,i]

x = np.zeros(n)

for i in range(n-1, -1, -1):
    soma = 0
    for j in range(i+1, n):
        soma += U[i,j]*x[j]
    x[i] = (y[i] - soma)/U[i,i]

print("Solução:")
print(x)

print("Verificação:")
print(np.dot(A, x))

print("Valores originais:")
print(b)
