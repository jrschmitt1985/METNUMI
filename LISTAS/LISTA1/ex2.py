import math

x = 5
valor_verdadeiro = 6.737947e-3
n = 20


soma_direta = 0
soma_exp_pos = 0

print("Termo    |    direta   | erro direta (%) |   inversa   | erro inversa (%)")

for i in range(n):
    soma_direta += ((-1)**i) * (x**i) / math.factorial(i)

    soma_exp_pos += (x**i) / math.factorial(i)
    soma_inversa = 1 / soma_exp_pos

erro_direta = abs((valor_verdadeiro - soma_direta) / valor_verdadeiro) * 100
erro_inversa = abs((valor_verdadeiro - soma_inversa) / valor_verdadeiro) * 100

print(f"{i+1}       | {soma_direta:.9f} |   {erro_direta:.9f}   | {soma_inversa:.9f} | {erro_inversa:.9f}")
