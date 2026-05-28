import numpy as np
import matplotlib.pyplot as plt

#Dados

# Conjunto 2 (trocando linha 2 e 3 , no A e b)
A = np.array([[5, 1, 1],[-1, 4, -1],[-1, 1, -3] ], dtype=float)

b = np.array([7, 4, 3], dtype=float)

# Resolução 

# Número de incógnitas
n = len(b)
 
# Aproximação inicial
x_old = np.zeros(n)

# Número máximo de casas significativas
na = 6

# Critério de parada
Eppara = (1 / 2) * 10 ** (2 - na)

# Inicializa erro alto
epest = np.ones(n) * 100

# Método de Gauss-Seidel
while np.max(epest) >= Eppara:

    x_new = np.copy(x_old)

    for i in range(n):

        soma = 0

        for j in range(n):
            if j != i:
                soma += A[i][j] * x_new[j]

        x_new[i] = (b[i] - soma) / A[i][i]

    # Cálculo do erro percentual estimado
    for i in range(n):
        if x_new[i] != 0:
            epest[i] = abs((x_new[i] - x_old[i]) / x_new[i]) * 100

    # Atualiza valores antigos
    x_old = np.copy(x_new)

# Resultado final
print("Solução:")
for i in range(n):
    print(f"x{i+1} = {x_old[i]:.6f}")
