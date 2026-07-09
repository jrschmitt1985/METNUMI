import numpy as np


valor_integral = 879/320   

a = 0
b = 1.5

def f(x):
    return 2 + x**3 - x**4

def f1(x):
    return 3*x**2 - 4*x**3   

def f2(x):
    return 6*x - 12*x**2     
def trap_multi(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        xk = a + k * h
        soma = soma + f(xk)
    return h / 2 * (f(a) + 2 * soma + f(b))

def erro_truncamento(a, b, n):
    f2_media = (f1(b) - f1(a)) / (b - a)   
    return -(b - a)**3 / (12 * n**2) * f2_media


n2 = trap_multi(f, a, b, 2)
ept_n2 = abs(valor_integral - n2) / valor_integral * 100
et2 = erro_truncamento(a, b, 2)


n4 = trap_multi(f, a, b, 4)
ept_n4 = abs(valor_integral - n4) / valor_integral * 100
et4 = erro_truncamento(a, b, 4)

print("O valor da integral com n = 2 é: ", n2)
print("Erro percentual verdadeiro (Ept) com n = 2 =", ept_n2, "%")
print("Erro de truncamento estimado (Et) com n = 2 =", et2)

print("O valor da integral com n = 4 é: ", n4) 
print("Erro percentual verdadeiro (Ept) com n = 4 =", ept_n4, "%")
print("Erro de truncamento estimado (Et) com n = 4 =", et4)
