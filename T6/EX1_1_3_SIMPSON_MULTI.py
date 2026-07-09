import numpy as np

valor_integral = 879/320

a = 0
b = 1.5

def f(x):
    return 2 + x**3 - x**4

def f3(x):
    return 6 - 24*x

def simpsom_multi(f, a, b, n):
    h = (b - a) / n
    soma_par = 0
    soma_impar = 0
    for k in range(1, n):
        xk = a + k * h
        if k % 2 == 0:
            soma_par += f(xk)
        else:
            soma_impar += f(xk)
    return (b - a) * (f(a) + 4 * soma_impar + 2 * soma_par + f(b)) / (3 * n)

def erro_truncamento(a, b, n):
    f4_media = (f3(b) - f3(a)) / (b - a)
    return -(b - a)**5 / (180 * n**4) * f4_media

n2 = simpsom_multi(f, a, b, 2)
ept_n2 = abs(valor_integral - n2) / valor_integral * 100
et2 = erro_truncamento(a, b, 2)

n4 = simpsom_multi(f, a, b, 4)
ept_n4 = abs(valor_integral - n4) / valor_integral * 100
et4 = erro_truncamento(a, b, 4)

print("O valor da integral com n = 2 é: ", n2)
print("Erro percentual verdadeiro (Ept) com n = 2 =", ept_n2, "%")
print("Erro de truncamento estimado (Et) com n = 2 =", et2)

print("O valor da integral com n = 4 é: ", n4)
print("Erro percentual verdadeiro (Ept) com n = 4 =", ept_n4, "%")
print("Erro de truncamento estimado (Et) com n = 4 =", et4)



    