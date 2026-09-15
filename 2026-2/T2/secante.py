def secante(f, xi_1, xi, Eppara):
    Epest = 100
    iteracao = 0

    while Epest >= Eppara:
        xi_new = xi - ((xi_1 - xi) / (f(xi_1) - f(xi))) * f(xi)
        iteracao += 1
        Epest = abs((xi_new - xi) / xi_new) * 100
        xi_1 = xi
        xi = xi_new

    return xi, Epest, iteracao
