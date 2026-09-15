def falsaPosicao(f, xl, xu, Eppara):
    xr_old = None
    Epest = 100
    iteracao = 0

    while Epest >= Eppara:
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
        iteracao += 1

        if xr_old is not None:
            Epest = abs((xr - xr_old) / xr) * 100

        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            Epest = 0

        xr_old = xr

    return xr, Epest, iteracao
