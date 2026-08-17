import math

x = 0.3*math.pi
n = 8
epest = 100
eppara = 0.5*10**(2-n)

def seriemcl(x, i):
    soma = 0
    for n in range(i):
        termo = ((-1)**n * x**(2*n)) / math.factorial(2*n)
        soma += termo
    return soma

print(f"Valor aproximado de cos({x}): {seriemcl(x,n):.8f}")