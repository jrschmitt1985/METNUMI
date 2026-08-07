import numpy as np

def f(x):
    return np.exp(-x)-x
 
# xi-1 = x_old
# xi = x  
# xi+1 = x_new

x_old = 0
x = 1
n=6
epest = 100
eppara = 0.5*10**(2-n)
iteracoes = 0


while epest >= eppara:
    x_new = x-((x_old-x)/(f(x_old)-f(x)))*f(x)

    epest = abs((x_new - x)/x_new)*100

    x_old = x
    x = x_new

    

    iteracoes += 1
print(f"Raíz: {x_new:.6f} | f(x) = {f(x_new):.2e} | Iterações: {iteracoes} | Erro: {epest:.6f}%") 