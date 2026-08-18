import math


def seriemcl(x,n):
    x = 0.3*math.pi
    n = 8
    epest = 100
    eppara = 0.5*10**(2-n)
    k = 0
    v_old = 0
    soma = 0


    while epest > eppara:
        termo = ((-1)**k * x**(2*k)) / math.factorial(2*k)
        soma += termo
        epest = 100
            

        if k > 0:
            # Calcula Epest entre a estimativa atual (soma) e a anterior (v_old)
            epest = ((soma - v_old)/soma) * 100
        v_old = soma
        k += 1 #vai para o proximo termo

    return soma, k




print(f"Valor aproximado de cos(x): {seriemcl(x,n):.8f}")