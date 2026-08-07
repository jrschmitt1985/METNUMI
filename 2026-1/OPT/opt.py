import math

def f(x):
    return (x**2)/10 - 2*math.sin(x)

xl = 0
xu = 4

phi = 1.6180

n = 6


eppara = 0.5 * (10 ** (2 - n))


epest = 100


iteracao = 0

while epest >= eppara:
    iteracao += 1

    d = (phi - 1) * (xu - xl)
    x1 = xl + d
    x2 = xu - d

    if f(x1) < f(x2):
        xl = x2
        Xopt = x1
    else:
        Xopt = x2
        xu = x1

    epest = (2 - phi) * ((xu - xl) / Xopt) * 100

    print(f"Iteração {iteracao}: Xopt = {Xopt:.6f}, Eppara = {eppara:.6f}, Epest = {epest:.6f}")

print(f"\nResultado final: Xopt = {Xopt:.6f}")