import numpy as np

def f(x):
    return (x**10)-1

i=6
eppara=0.5*(10**(2-1))

x=np.linspace(0,1.3,100)
intervalos=[]

for i in range (len(x)-1):
    if (f(x[i]) * f(x[i+1]) <0):
        intervalos.append([x[i], x[i+1]])

print(f"Intervalos encontrados: {len(intervalos)}")

for idx, 