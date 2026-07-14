import numpy as np
from sympy import E

def f1(x,y):
    return y + x ** 2 - x - 0.5
def f2(x,y):
    return y + 5 * x * y - x ** 2
def df1_dx(x,y):
    return 2*x - 1
def df1_dy(x,y):
    return 1
def df2_dx(x,y):
    return 5*y-2*x
def df2_dy(x,y):
    return 1 + 5*x

Epest=np.array([100, 100])

Eppara = 0.5*10**(2-6)
x_old = np.array([1.2 , 1.2])

print("Valores iniciais: ", x_old)

iteracoes = 0



while np.max(Epest) >= Eppara:
    

    x = x_old[0]
    y = x_old[1]

    numerador_x = (f1(x,y) * df2_dy(x,y)) - (f2(x,y)*df1_dy(x,y))

    numerador_y = (f2(x,y) * df1_dx(x,y)) - (f1(x,y)*df2_dx(x,y))
    denominador = ((df1_dx(x,y)*df2_dy(x,y))-(df1_dy(x,y)*df2_dx(x,y)))

    
    x_new = x-(numerador_x/denominador)
    y_new = y-(numerador_y/denominador)

    solucao_new = np.array([x_new, y_new])

    Epest = np.abs((solucao_new - x_old)/solucao_new)*100

    x_old = solucao_new.copy()
    iteracoes += 1

print(f"Solução: ({x_old[0]:.6f}, {x_old[1]:.6f})")
print("Iterações:", iteracoes)
print(f"Erro: {np.max(Epest):.13f}%")