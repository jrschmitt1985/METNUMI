import numpy as np

def f1(x1,x2):
    return (x2) + (x1**2) - x1 -1/2

def f2(x1,x2):
    return x2 + (5*x1*x2) - (x1**2)

def df1_dx1(x1,x2):
    return (2*x1) - 1

def df1_dx2(x1,x2):
    return 1

def df2_dx1(x1,x2):
    return 5*x2 - 2*x1

def df2_dx2(x1,x2):
    return 1 + 5*x1


x_old = np.array([1.2, 1.2])

print("Valores iniciais: ", x_old)

epest=np.array([100, 100])

i = 6
eppara = 0.5 * (10 ** (2 - i))

#contador de iteracoes
iteracoes= 0

while np.max(epest) >= eppara:

    iteracoes += 1

    x1_old = x_old[0]
    x2_old = x_old[1]
    
    x1_new = x1_old - ((f1(x1_old,x2_old)*df2_dx2(x1_old,x2_old) - f2(x1_old,x2_old)*df1_dx2(x1_old,x2_old))/(df1_dx1(x1_old,x2_old)*df2_dx2(x1_old,x2_old) - df1_dx2(x1_old,x2_old)*df2_dx1(x1_old,x2_old)))

    x2_new = x2_old - ((f2(x1_old,x2_old)*df1_dx1(x1_old,x2_old) - f1(x1_old,x2_old)*df2_dx1(x1_old,x2_old))/(df1_dx1(x1_old,x2_old)*df2_dx2(x1_old,x2_old) - df1_dx2(x1_old,x2_old)*df2_dx1(x1_old,x2_old)))
    
    x_new = np.array([x1_new, x2_new])

    epest = np.abs((x_new - x_old)/x_new)*100

    x_old = x_new.copy()


print(f"Solução: ({x_new[0]:.6f}, {x_new[1]:.6f})")
print("Iterações:", iteracoes)