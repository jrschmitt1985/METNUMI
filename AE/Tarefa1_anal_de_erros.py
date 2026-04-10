import numpy as np
import math
import matplotlib.pyplot as plt

# Dados Iniciais
x = 0.3
n = 6
u = math.log(1 + x)



# Pré-alocação

soma = 0
estimativa = []
contador = []
EPT = []
EPEST = []
v_old = 0

# Variáveis de controle do while
i = 1
eppara = 0.5*(10**(2-n))
epest = 100
Ept = 100

# Série de MacLaurin
def ex(x,i):
    return ((-1)**(i+1)) * (x**i)/i

while epest > eppara and Ept > eppara:
    
    soma = soma + ex(x,i) 
    v_new = soma
    Ept = abs((u - soma)/u)*100

    if i > 1:
        epest = abs((v_new - v_old)/v_new)*100
        erro = abs(v_new - v_old)
        EPEST.append(epest)
        
    # Atualização
    v_old = v_new
        
    EPT.append(Ept)
    estimativa.append(soma)
    contador.append(i)





plt.figure()
plt.plot(contador,estimativa,'or',label="$ln(1+x)$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Estimativa")
plt.grid()

plt.figure()
plt.plot(contador,EPT,'ok',label="$E_{pt}$")
plt.plot(contador[1:],EPEST,'og',label="$E_{pest}$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("E_{pt}$ (%)")
plt.grid()

print("Valor real =", u)
print("Última estimativa =", estimativa[-1])
print("Número de termos usados =", len(contador))
print("Último erro =", erro)

plt.show()


#TAREFA DE CASA FAZER O PROGRAMA PARAR ATÉ A SEXTA CASA DECIMAL USANDO WHILE
#
jj
