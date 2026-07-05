import numpy as np

A = np.array([[10 , 2, -1],
              [-3, -5, 2],
              [1, 1, 5]])

b = np.array([27, -61.5, -21.5])

n = len(b)

na = 6
Eppara = 0.5*10**(2 - na)
print(Eppara)
# Chute Inicial
x_old = np.ones(n)

#relaxamento
#relax = 1


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
        #x_new = relax*x_new + (1 - relax) * x_old
    
    Epest = np.abs((x_new - x_old)/x_new)*100
    
    x_old = x_new.copy()
    k += 1
    print(k)
print(x_new.copy())
            


        
