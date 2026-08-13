import numpy as np

def f(x):
    return np.log(x)

x_old = 0.5
x = 5

n = 6
iteracoes = 0

epest = 100
eppara = 0.5*10**(2-n)

while epest >= eppara:
    x_new = x-((x_old-x)/(f(x_old)-f(x)))*f(x)
   
    if x_new <= 0:
        print("O método da secante saiu do domínio da função (ln x).")
        break


    if iteracoes > 0:
        epest = abs((x_new - x)/x_new)*100
        
    x_old = x
    x = x_new
    iteracoes += 1
    


print(f"Raiz: {x_new:.6f} | f(x) = {f(x_new):.2e} | Iterações: {iteracoes:.6f} | Erro: {epest:.6f}%")