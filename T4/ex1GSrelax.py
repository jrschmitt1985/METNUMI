import numpy as np

A = np.array([[130, -30, 0],
              [-90, 90, -0],
              [-40, -60, 120]])

b = np.array([200, 0, 500])


k = 0
n = len(b)
xold = np.zeros(n)
eppara = 0.5 * (10 ** (2 - 6))
xnew = np.zeros(n)
epest = np.ones(n) * 100
maxit = 100

relaxamento = 1.1

while np.max(epest) >= eppara and k < maxit:
    for i in range(n):
        soma1 = 0
        soma2 = 0
        for j in range(n):
            if j < i:
                soma1 += A[i, j] * xnew[j]
            elif j > i:
                soma2 += A[i, j] * xold[j]
        xnew[i] = (b[i] - soma1 - soma2) / A[i, i]

    xnew = relaxamento * xnew + (1 - relaxamento) * xold  
    epest = np.abs((xnew - xold) / xnew) * 100
    xold = xnew.copy()
    k += 1

print("Solução:", xnew)
print("Número de iterações:", k)