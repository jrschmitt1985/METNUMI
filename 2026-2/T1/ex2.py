import math

x = 5
u = math.e**-x
n = 6
eppara = 0.5*10**(2-n)

#soma direta

soma_direta = 0
v_old_direta = 0
epest_direta = 100
k_direta = 0

while epest_direta > eppara:
    termo = ((-1)**k_direta * x**k_direta) / math.factorial(k_direta)
    soma_direta += termo

    if k_direta > 0:
        epest_direta = abs((soma_direta - v_old_direta)/soma_direta)

    v_old_direta = soma_direta
    k_direta += 1

print(f"Termos: {k_direta} | Resultado: {soma_direta:.8f}")

#soma inversa

soma_exp_pos = 0
v_old_inversa = 0
epest_inversa = 100
k_inversa = 0

while epest_inversa > eppara:
    termo = (x**k_inversa) / math.factorial(k_inversa)
    soma_exp_pos += termo
      
    v_new_inversa = 1 / soma_exp_pos
    
    if k_inversa > 0:
        epest_inversa = abs((v_new_inversa - v_old_inversa) / v_new_inversa) * 100
    
    v_old_inversa = v_new_inversa
    k_inversa += 1

print(f"Termos: {k_inversa} | Resultado: {v_new_inversa:.8f}")

ept_direta = abs((u - soma_direta) / u) * 100
ept_inversa = abs((u - v_new_inversa) / u) * 100

print("\n--- RESULTADO FINAL ---")
print(f"Método Direto : {soma_direta:.8f} | Ept: {ept_direta:.6f}% | Termos: {k_direta}")
print(f"Método Inverso: {v_new_inversa:.8f} | Ept: {ept_inversa:.6f}% | Termos: {k_inversa}")