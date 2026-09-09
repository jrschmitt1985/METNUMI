import numpy as np

def newton_raphson(f, df, x0, es, max_iter=100):
    xi = x0
    iteracao = 0
    historico = []
    while iteracao < max_iter:
        der = df(xi)
        if der == 0:
            break
        xi_novo = xi - f(xi) / der
        iteracao += 1
        epest = 100.0
        if xi_novo != 0:
            epest = abs((xi_novo - xi) / xi_novo) * 100.0
        historico.append(epest)
        xi = xi_novo
        if epest < es:
            break
    return xi, iteracao, epest, historico