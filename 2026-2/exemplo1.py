import numpy as np
import matplotlib.pyplot as plt
import math

#dados iniciais
x = 1
n = 6
u = 2.71828182846


#série mclaurin


def serieMclarium(x,n):
    return (x**n)/math.factorial(n)

#peé-alocação de memória

soma = 0
estimativa = []
contador = []
EPT = []
EPEST = [100]
v_old = 0


for i in range(n):
    soma = soma + serieMclarium(x,i)
    v_new = soma
    Ept = np.abs((u - soma)/u)*100

    if i > 0:
        Epest = np.abs((v_new - v_old)/v_new)*100
        EPEST.append(Epest)

    # Atualização
    v_old = v_new
    EPT.append(Ept)
    estimativa.append(soma)
    contador.append(i)

print(f"iteracoes: {i}")
print(f"soma: {soma}")
print(f"aproximacao: {v_new}")
print(f"erro: {Ept}")

plt.figure()
plt.plot(contador,estimativa, 'or', label="$e^x$")
plt.legend()
plt.xlabel("Numero de termos")
plt.ylabel("estimativa")
plt.grid()

plt.figure()
plt.plot(contador,EPT,'ok',label="E_{pt}$")
plt.plot(contador,EPEST,'og',label="E_{pt}$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("E_{pt}$ (%)")
plt.grid()

plt.show()