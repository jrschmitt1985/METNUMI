import numpy as np

def secante(f, x0, x1, es, max_iter=100):
    x_prev = x0
    x_curr = x1
    iteracao = 0
    historico = []
    while iteracao < max_iter:
        f_curr = f(x_curr)
        f_prev = f(x_prev)
        if f_curr - f_prev == 0:
            break
        x_next = x_curr - (f_curr * (x_prev - x_curr)) / (f_prev - f_curr)
        iteracao += 1
        epest = 100.0
        if x_next != 0:
            epest = abs((x_next - x_curr) / x_next) * 100.0
        historico.append(epest)
        x_prev = x_curr
        x_curr = x_next
        if epest < es:
            break
    return x_curr, iteracao, epest, historico