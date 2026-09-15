def secante(f, xi_1, xi, Eppara, max_iter=1000):
    Epest = 100
    iteracao = 0

    while Epest > Eppara and iteracao < max_iter:
        denominador = f(xi_1) - f(xi)

        if denominador == 0:
            raise ValueError("Divisão por zero no método da Secante.")

        xi_new = xi - ((xi_1 - xi) / denominador) * f(xi)
        iteracao += 1

        if xi_new != 0:
            Epest = abs((xi_new - xi) / xi_new) * 100

        xi_1 = xi
        xi = xi_new

    return xi, Epest, iteracao