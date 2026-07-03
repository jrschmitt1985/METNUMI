import numpy as np

A = np.array([[2, 4, -6],
              [4, 2, 2],
              [2, 8, -4]])

b = np.array([10, 16, 24])

n = len(b)

na = 12
Eppara = 0.5*10**(2 - na)
print(Eppara)
# Chute Inicial
x_old = np.ones(n)

# Alocação de Memória
k = 0
x_new = np.zeros(n)
Epest = np.linspace(100,100,n)
maxit = 100

while (np.max(Epest) > Eppara):
    
    for i in range (0,n):

        soma1 = 0
        soma2 = 0
        for j in range(0,n):

            if j < i:
                soma1 += A[i,j]*x_new[j]
            
            elif j > i:
                soma2 += A[i,j]*x_old[j]                
    
        x_new[i] = 1/A[i,i]*(b[i] - soma1 - soma2)
    
    Epest = np.abs((x_new - x_old)/x_new)*100
    
    x_old = x_new.copy()
    k += 1
    print(k)
print(x_new.copy())
            


        
