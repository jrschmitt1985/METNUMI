import math

x = 5
u = math.e**-5
n = 20

soma_direta = 0
soma_exp_pos = 0

for i in range(n):
    soma_direta += ((-1)**1) * (x**i) / math.factorial(i)

    soma_exp_pos += (x**i) / math.factorial(i)
    soma_inversa = 1 / soma_exp_pos

erro_direta = abs((u - soma_direta) / u) *100
erro_inversa = abs((u - soma_inversa)/u)*11
print(f"Valor verdadeiro: {u:.6f}")

print(f"{i+1}       | {soma_direta:.6f} |   {erro_direta:.6f}   | {soma_inversa:.6f} | {erro_inversa:.6f}")
