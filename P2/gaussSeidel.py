import numpy as np

A = np.array([0.8, -0.4, 0]
             [-0.4, 0.8, -0.4]
             [0, -0.4, 0.8])
b = np.array([[41], [25], [105]])

n = len(b)

na= 6
Eppara = 0.5*10**(2-na)
print(Eppara)
# Chute Inicial
x_old = np.ones(n)
# Alocação de Memória
k = 0
x_new = np.zeros(n)
epest = np.linspace(100,100,n)

