
import numpy as np

A1 = np.array([[8, 3, 1],
               [-6, 0, 7],
               [2, 4, -1]], dtype=float)
b1 = np.array([12, 1, 5])

A2 = np.array([[1, 1, 5],
               [-1, 4, -1],
               [3, 1, -1]], dtype=float)
b2 = np.array([7, 4, 3])

A3 = np.array([[-7, 3, 5],
               [-2, 4, -5],
               [0, 2, -1]], dtype=float)
b3 = np.array([7, -3, 1])

matrizes = [A1, A2, A3]
vetores = [b1, b2, b3]
ordens = [[0, 2, 1], [2, 1, 0], [0, 2, 1]]

eppara = 0.5 * 10**(2-6)

for c in range(3):

    A = matrizes[c].copy()
    b = vetores[c].copy()
    n = len(b)

    print("Conjunto", c+1)
    print("Ordem original:")

    if A[0,0] == 0 or A[1,1] == 0 or A[2,2] == 0:
        print("Nao pode calcular: existe zero na diagonal.")

    else:
        xold = np.zeros(n)

        for k in range(8):
            xnew = xold.copy()

            for i in range(n):
                soma = 0
                for j in range(n):
                    if j != i:
                        soma += A[i,j] * xnew[j]

                xnew[i] = (b[i] - soma) / A[i,i]

            print("Iteracao", k+1, ":", xnew)
            xold = xnew.copy()

    A = A[ordens[c]]
    b = b[ordens[c]]

    xold = np.zeros(n)
    epest = np.ones(n) * 100
    k = 0

    while max(epest) >= eppara and k < 100:
        xnew = xold.copy()

        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i,j] * xnew[j]

            xnew[i] = (b[i] - soma) / A[i,i]

        for i in range(n):
            if xnew[i] != 0:
                epest[i] = abs((xnew[i] - xold[i]) / xnew[i]) * 100
            else:
                epest[i] = 100

        xold = xnew.copy()
        k += 1

    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)

    T = -np.linalg.inv(D + L) @ U

    autovalores = np.linalg.eigvals(T)
    raio = max(abs(autovalores))

    print("Raio espectral:", raio)
    print("Solucao com equacoes reorganizadas:")
    print(xnew)
    print("Numero de iteracoes:", k)
    print("Erro percentual:", epest)
    print("Verificacao:", np.dot(A, xnew))
    print("Valores originais:", b)
    print()
