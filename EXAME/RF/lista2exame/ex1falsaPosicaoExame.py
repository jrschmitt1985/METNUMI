import numpy as np

def f(x):
    return np.sin(4*x) + np.cos(3*x)

x = np.linspace(0, 2*np.pi, 100)
intervalos=[]

i = 8
eppara = 0.5*10**(2-i)


for i in range(len(x)-1):
    if (f(x[i])*f(x[i+1])<0):
        intervalos.append([x[i], x[i+1]])

print(f"Intervalos encontrados:, {len(intervalos)}\n")

print("Os intervalos encontrados são:")
for xl, xu in intervalos:
    
    print(f"[{xl:.6f}, {xu:.6f}]")

for idx, (xl, xu) in enumerate(intervalos):
    epest = 100
    xr_ant= (xl + xu)/2
    iteracoes=0

    while epest >= eppara:
        xr = xu - (f(xu)*(xl-xu)/(f(xl)-f(xu)))
        f_xl = f(xl)
        f_xr = f(xr)

        if iteracoes > 0:
            epest = abs((xr-xr_ant)/xr)*100
        if f_xr * f_xl < 0:
            xu = xr
        else:
            xl = xr
        xr_ant=xr
        iteracoes += 1

    print(f"Raíz {idx+1}: x= {xr:.6f} | f(x) = {f(xr):.2e} | iterações: {iteracoes}")
