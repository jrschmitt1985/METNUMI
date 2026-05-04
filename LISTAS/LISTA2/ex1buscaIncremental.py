import numpy as np

def f(x):
    return np.sin(4*x) + np.cos(3*x)

x = np.linspace(0, 2*np.pi, 100)
y = f(x)

xb = []
nb = 0

for i in range(len(x)-1):
    xl = x[i]
    xu = x[i+1]

    if (f(xl)*f(xu) < 0):
        nb += 1
        xb.append([xl,xu])
    if not xb:
        print("Nenhum subintervalo foi encontrado!")

        exit()

print("xb = ", xb)
print("y = ", f(x))
print("Número de intervalos com raiz" , nb)
