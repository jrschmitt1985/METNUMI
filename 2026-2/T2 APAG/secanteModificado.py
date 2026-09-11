import numpy as np

def secante_modificado(f, x0, delta=1e-5, es=1e-5, max_iter=100):
    xi = x0
    iteracao = 0
    historico = []
    while iteracao < max_iter:
        f_xi = f(xi)
        f_pert = f(xi + delta * xi)
        if f_pert - f_xi == 0:
            break
        xi_novo = xi - (delta * xi * f_xi) / (f_pert - f_xi)
        iteracao += 1
        epest = 100.0
        if xi_novo != 0:
            epest = abs((xi_novo - xi) / xi_novo) * 100.0
        historico.append(epest)
        xi = xi_novo
        if epest < es:
            break
    return xi, iteracao, epest, historico