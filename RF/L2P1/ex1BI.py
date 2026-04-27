import numpy as np

def f(x):
    return np.sin(4*x) + np.cos(3*x)
x=np.linspace(0,2*np.pi,1000)
xb=[]
nb=0
n=1000
for i in range(n-1):
    xl=x[i]
    xu=x[i+1]
    if (f(xl)*f(xu)<0):
        nb+=1
        xb.append([xl,xu])
else:
    print("Não há raíz entre",xl,"e",xu)
print("xb=",xb)
print("y=",f(x))
print("Número de intervalos com raíz:", nb)