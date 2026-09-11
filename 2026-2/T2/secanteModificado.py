def secanteModificado(f, xi, delta, Eppara, max_iter=1000):
    Epest = 100
    iteracao = 0

    while Epest > Eppara and iteracao < max_iter:
        denominador = f(xi + delta * xi) - f(xi)

        if denominador == 0:
            raise ValueError("Divisão por zero no método da Secante Modificado.")

        xi_new = xi - (delta * xi * f(xi)) / denominador
        iteracao += 1

        if xi_new != 0:
            Epest = abs((xi_new - xi) / xi_new) * 100

        xi = xi_new

    return xi, Epest, iteracao