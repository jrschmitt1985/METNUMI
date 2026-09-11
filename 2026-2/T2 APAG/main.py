import numpy as np
from bisseccao import bisseccao
from falsaPosicao import falsa_posicao
from newtonRaphson import newton_raphson
from secante import secante
from secanteModificado import secante_modificado

es = 0.5 * 10**(2 - 6)

equacoes = {
    'a': {'f': lambda x: x**5 - x - 1, 'df': lambda x: 5*x**4 - 1, 'xl': 1.0, 'xu': 2.0, 'x0': 1.5, 'x1': 2.0},
    'b': {'f': lambda x: x + np.tan(x), 'df': lambda x: 1 + (1/np.cos(x))**2, 'xl': 2.0, 'xu': 3.0, 'x0': 2.5, 'x1': 3.0},
    'c': {'f': lambda x: (x + 1)**0.5 - x**(-2), 'df': lambda x: 0.5*(x + 1)**(-0.5) + 2*x**(-3), 'xl': 0.5, 'xu': 1.5, 'x0': 1.0, 'x1': 1.5},
    'd': {'f': lambda x: 2*x - 2*x**2 + 1, 'df': lambda x: 2 - 4*x, 'xl': 1.0, 'xu': 2.0, 'x0': 1.2, 'x1': 1.5},
    'e': {'f': lambda x: np.log(x) - 3*np.exp(x + 2), 'df': lambda x: 1/x - 3*np.exp(x + 2), 'xl': 0.0001, 'xu': 0.01, 'x0': 0.001, 'x1': 0.005},
    'f': {'f': lambda x: np.log(x) + (x + 1)**3, 'df': lambda x: 1/x + 3*(x + 1)**2, 'xl': 0.1, 'xu': 1.0, 'x0': 0.2, 'x1': 0.5},
    'g': {'f': lambda x: x**2 - np.cos(x), 'df': lambda x: 2*x + np.sin(x), 'xl': 0.5, 'xu': 1.5, 'x0': 0.8, 'x1': 1.2},
    'h': {'f': lambda x: np.exp(-x**2) - x**2 - 2*x + 2, 'df': lambda x: -2*x*np.exp(-x**2) - 2*x - 2, 'xl': 0.0, 'xu': 1.0, 'x0': 0.5, 'x1': 0.8}
}

def fmt_val(val, fmt=":.6f"):
    return f"{val:{fmt[1:]}}" if val is not None else "Sem raiz"

def fmt_err(val):
    return f"{val:.6e}" if val is not None else "N/A"

print(f"{'Eq':<3} | {'Método':<18} | {'Raiz':<12} | {'Iters':<6} | {'Erro (%)':<10}")
print("-" * 65)

for item, eq in equacoes.items():
    f, df = eq['f'], eq['df']
    xl, xu, x0, x1 = eq['xl'], eq['xu'], eq['x0'], eq['x1']
    
    # Suprime avisos do numpy ao calcular log em pontos inválidos
    with np.errstate(all='ignore'):
        r_bis, i_bis, e_bis, _ = bisseccao(f, xl, xu, es)
        r_fal, i_fal, e_fal, _ = falsa_posicao(f, xl, xu, es)
        r_new, i_new, e_new, _ = newton_raphson(f, df, x0, es)
        r_sec, i_sec, e_sec, _ = secante(f, x0, x1, es)
        r_mod, i_mod, e_mod, _ = secante_modificado(f, x0, es=es)
    
    print(f"{item:<3} | Bissecção          | {fmt_val(r_bis):<12} | {i_bis:<6} | {fmt_err(e_bis)}")
    print(f"{item:<3} | Falsa Posição      | {fmt_val(r_fal):<12} | {i_fal:<6} | {fmt_err(e_fal)}")
    print(f"{item:<3} | Newton-Raphson     | {fmt_val(r_new):<12} | {i_new:<6} | {fmt_err(e_new)}")
    print(f"{item:<3} | Secante            | {fmt_val(r_sec):<12} | {i_sec:<6} | {fmt_err(e_sec)}")
    print(f"{item:<3} | Secante Modificado | {fmt_val(r_mod):<12} | {i_mod:<6} | {fmt_err(e_mod)}")
    print("-" * 65)