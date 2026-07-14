import numpy as np
A = np.array ([[0.8, -0.4, 0],
                 [-0.4, 0.8, -0.4],
                 [0, -0.4, 0.8]])
b = np.array ([41, 25, 105])


n = len(b)
Epest = np.linspace(100,100,n)
Eppara = 0.5*10**(2-6)
maxit = 100
x_old = np.ones(n)
k=0
x_new = np.zeros(n)


while max(Epest) > Eppara and k < 100:

    for i in range(n):

        soma = 0
        
        for j in range(n):

            if j != i:
                soma += A[i,j]*x_new[j]
            
        x_new[i] = (b[i] - soma) / A[i,i]
    
    Epest = ((x_new - x_old)/x_new)*100
    x_old = x_new.copy()
    k += 1
print(k)
print(x_new.copy())
