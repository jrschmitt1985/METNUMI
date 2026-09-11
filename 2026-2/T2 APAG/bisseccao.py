import numpy as np

def bisseccao(f, xl, xu, es, max_iter=100):
    if f(xl) * f(xu) >= 0:
        return None, 0, None, []
    xr = xl
    iteracao = 0
    historico = []
    while iteracao < max_iter:
        xr_antigo = xr
        xr = (xl + xu) / 2.0
        iteracao += 1
        epest = 100.0
        if iteracao > 1 and xr != 0:
            epest = abs((xr - xr_antigo) / xr) * 100.0
        historico.append(epest)
        if iteracao > 1 and epest < es:
            break
        teste = f(xl) * f(xr)
        if teste < 0:
            xu = xr
        elif teste > 0:
            xl = xr
        else:
            break
    return xr, iteracao, epest, historico