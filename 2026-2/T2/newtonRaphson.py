def newtonRaphson(f, df, xi, Eppara):
    Epest = 100
    iteracao = 0

    while Epest >= Eppara:
        xi_new = xi - f(xi) / df(xi)
        iteracao += 1
        Epest = abs((xi_new - xi) / xi_new) * 100
        xi = xi_new

    return xi, Epest, iteracao
