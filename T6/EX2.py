from sympy import symbols, sqrt, tanh, integrate, N
import math

g = 9.8
m = 68.1
cd = 0.25

t0 = 0
t10 = 10
t = symbols('t')

v = sqrt((g * m) / cd) * tanh(sqrt((g * cd) / m) * t)

tempo = integrate(v, (t, t0, t10))

print("A integral da função v(t) no intervalo de 0 a 10 é:", N(tempo))

def v(t):
    return math.sqrt(g * m / cd) * math.tanh(math.sqrt(g * cd / m) * t)


def trap_multi(f, t0, t10, n):
    h = (t10 - t0) / n
    soma = 0
    for k in range(1, n):
        soma += f(t0 + k * h)
    return h/2 * (f(t0) + 2 * soma + f(t10))

def simpson_multi(f, t0, t10, n):
    h = (t10 - t0) / n
    soma_impar = 0
    soma_par = 0
    for k in range(1, n):
        xk = t0 + k * h
        if k % 2 != 0:
            soma_impar += f(xk)
        else:
            soma_par += f(xk)
    return (t10 - t0) * (f(t0) + 4 * soma_impar + 2 * soma_par + f(t10)) / (3*n)

criterio = 0.5e-6   

# Trapezio 
n = 1
while True:
    resultado = trap_multi(v, t0, t10, n)
    erro_relativo = abs(tempo - resultado) / abs(tempo)
    if erro_relativo < criterio:
        print(f"Trapezio convergiu com n = {n}, resultado = {resultado:.8f}, erro relativo = {erro_relativo:.2e}")
        break
    n += 1

#  Simpson 1/3 
n = 2
while True:
    resultado = simpson_multi(v, t0, t10, n)
    erro_relativo = abs(tempo - resultado) / abs(tempo)
    if erro_relativo < criterio:
        print(f"Simpson convergiu com n = {n}, resultado = {resultado:.8f}, erro relativo = {erro_relativo:.2e}")
        break
    n += 2   


