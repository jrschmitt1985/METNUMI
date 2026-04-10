import numpy as np
import math
import matplotlib.pyplot as plt

def calcular_ln(x, n):
    # Valor real
    u = math.log(1 + x)

    # Inicialização
    soma = 0
    estimativa = []
    contador = []
    EPT = []
    EPEST = []
    v_old = 0

    i = 1
    eppara = 0.5*(10**(2-n))
    epest = 100

    # Série de Maclaurin
    def ex(x,i):
        return ((-1)**(i+1)) * (x**i)/i

    while epest > eppara:
        
        soma = soma + ex(x,i) 
        v_new = soma
        
        # erro verdadeiro percentual
        Ept = abs((u - soma)/u)*100
        
        # erro aproximado percentual
        if i > 1:  # 👈 importante!
            epest = abs((v_new - v_old)/v_new)*100
        
        # armazenando
        EPT.append(Ept)
        EPEST.append(epest)
        estimativa.append(soma)
        contador.append(i)
        
        v_old = v_new
        i += 1

    # Resultados
    print(f"\n===== RESULTADOS PARA x = {x} =====")
    print("Valor real =", u)
    print("Última estimativa =", estimativa[-1])
    print("Número de termos usados =", len(contador))
    print("Último erro aproximado =", epest)

    return contador, estimativa, EPT, EPEST


# 🔹 Rodando para dois valores
x1 = 0.5
x2 = 0.9

c1, est1, ept1, epest1 = calcular_ln(x1, 10)
c2, est2, ept2, epest2 = calcular_ln(x2, 10)


# 📈 Gráfico estimativa
plt.figure()
plt.plot(c1, est1, 'or', label=f"x={x1}")
plt.plot(c2, est2, 'ob', label=f"x={x2}")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Estimativa")
plt.grid()

# 📉 Gráfico erros
plt.figure()
plt.plot(c1, ept1, 'or', label=f"Ept x={x1}")
plt.plot(c2, ept2, 'ob', label=f"Ept x={x2}")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Erro (%)")
plt.grid()

plt.show()