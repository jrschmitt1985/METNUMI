def secanteModificado(f, xi, delta, Eppara):
    Epest = 100
    iteracao = 0

    while Epest >= Eppara:
        xi_new = xi - (delta * xi * f(xi)) / (f(xi + delta * xi) - f(xi))
        iteracao += 1
        Epest = abs((xi_new - xi) / xi_new) * 100
        xi = xi_new

    return xi, Epest, iteracao
