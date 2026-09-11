import numpy as np
from bisseccao import bisseccao
from newtonRaphson import newton_raphson

f = lambda x: np.exp(-x) - 2 * np.sqrt(x)
df = lambda x: -np.exp(-x) - 1 / np.sqrt(x)

es = 0.5 * 10**(2 - 6)

r_bis, i_bis, e_bis, _ = bisseccao(f, 0.0001, 1.0, es)
r_new, i_new, e_new, _ = newton_raphson(f, df, 0.5, es)

print(f"Bissecção: Raiz = {r_bis:.6f} | Iterações = {i_bis} | Erro = {e_bis:.8f}%")
print(f"Newton-Raphson: Raiz = {r_new:.6f} | Iterações = {i_new} | Erro = {e_new:.8f}%")