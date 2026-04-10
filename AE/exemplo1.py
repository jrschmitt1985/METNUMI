import numpy as np
import math
import matplotlib.pyplot as plt

# Dados Iniciais
x = 1
n = 6
u= math.exp(1)

# Série de MacLaurin
def ex(x,n):
    return x**n/math.factorial(n)

#Pré-alocação

soma = 0
estimativa = []
contador = []
EPT = []
EPEST = [100]
v_old = 0



for i in range(n):
    
    soma = soma + ex(x,i) 
    v_new = soma
    Ept = abs((u - soma)/u)*100
    
    if i > 0:
        Epest = abs((v_new - v_old)/v_new)*100
        EPEST.append(Epest)
        
    # Atualização
    v_old = v_new
        
    EPT.append(Ept)
    estimativa.append(soma)
    contador.append(i)

plt.figure()
plt.plot(contador,estimativa,'or',label="$e^x$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Estimativa")
plt.grid()

plt.figure()
plt.plot(contador,EPT,'ok',label="E_{pt}$")
plt.plot(contador,EPEST,'og',label="E_{pt}$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("E_{pt}$ (%)")
plt.grid()



#TAREFA DE CASA FAZER O PROGRAMA PARAR ATÉ A SEXTA CASA DECIMAL USANDO WHILE
