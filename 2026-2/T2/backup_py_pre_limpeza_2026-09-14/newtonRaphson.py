def newtonRaphson(f, df, xi, Eppara, max_iter=1000):
    Epest = 100
    iteracao = 0

    while Epest > Eppara and iteracao < max_iter:
        if df(xi) == 0:
            raise ValueError("Derivada igual a zero.")

        xi_new = xi - f(xi) / df(xi)
        iteracao += 1

        if xi_new != 0:
            Epest = abs((xi_new - xi) / xi_new) * 100

        xi = xi_new

    return xi, Epest, iteracao