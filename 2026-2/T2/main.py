import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from bisseccao import bisseccao
from falsaPosicao import falsaPosicao
from newtonRaphson import newtonRaphson
from secante import secante
from secanteModificado import secanteModificado


def fA(x):
    return x**5 - x - 1


def dfA(x):
    return 5*x**4 - 1


def fB(x):
    return x + np.tan(x)


def dfB(x):
    return 1 + 1/np.cos(x)**2


def fC(x):
    return np.sqrt(x + 1) - x**(-2)


def dfC(x):
    return 1/(2*np.sqrt(x + 1)) + 2*x**(-3)


def fD(x):
    return 2**x - 2*x**2 + 1


def dfD(x):
    return np.log(2)*2**x - 4*x


def fE(x):
    return np.log(x) - 3*np.exp(x + 2)


def dfE(x):
    return 1/x - 3*np.exp(x + 2)


def fF(x):
    return np.log(x) + (x + 1)**3


def dfF(x):
    return 1/x + 3*(x + 1)**2


def fG(x):
    return x**2 - np.cos(x)


def dfG(x):
    return 2*x + np.sin(x)


def fH(x):
    return np.exp(-x**2) - x**2 - 2*x + 2


def dfH(x):
    return -2*x*np.exp(-x**2) - 2*x - 2


def f2(x):
    return np.exp(-x) - 2*np.sqrt(x)


def df2(x):
    return -np.exp(-x) - 1/np.sqrt(x)


def buscaIncremental(f, faixas, dx):
    intervalos = []

    for inicio, fim in faixas:
        x = inicio

        while x < fim:
            x2 = min(x + dx, fim)

            if f(x) * f(x2) < 0:
                intervalos.append((x, x2))

            x = x2

    return intervalos


def exibirResultado(nome, xr, Epest, iteracao):
    print(f"{nome}:")
    print("xr =", xr)
    print("Epest =", Epest)
    print("Iterações =", iteracao)


def formatarGrafico():
    formato = FuncFormatter(lambda valor, pos: f"{valor:g}".replace(".", ","))
    eixo = plt.gca()
    eixo.xaxis.set_major_formatter(formato)
    eixo.yaxis.set_major_formatter(formato)
    plt.xlabel("x")
    plt.ylabel("f(x)")


n = 6
Eppara = 0.5 * (10 ** (2 - n))
delta = 0.0000001
dx = 0.01

casos = [
    ("a", fA, dfA, [(-3, 3)], False),
    ("b", fB, dfB, [(np.pi/2 + 0.01, np.pi - 0.01)], True),
    ("c", fC, dfC, [(-0.999, -0.01), (0.01, 5)], False),
    ("d", fD, dfD, [(-5, 10)], False),
    ("e", fE, dfE, [(0.001, 10)], False),
    ("f", fF, dfF, [(0.001, 5)], False),
    ("g", fG, dfG, [(-3, 3)], False),
    ("h", fH, dfH, [(-5, 5)], False)
]

for nome, f, df, faixas, raizesInfinitas in casos:
    intervalos = buscaIncremental(f, faixas, dx)

    print(f"\nFunção {nome}")

    if raizesInfinitas:
        print("Número de raízes reais: infinitas")
    else:
        print("Número de raízes reais:", len(intervalos))

    intervalosPositivos = [intervalo for intervalo in intervalos if intervalo[1] > 0]

    if not intervalosPositivos:
        print("Não foi encontrada raiz positiva.")
        continue

    xl, xu = min(intervalosPositivos, key=lambda intervalo: intervalo[1])
    xi = (xl + xu) / 2

    xr, Epest, iteracao = bisseccao(f, xl, xu, Eppara)
    exibirResultado("Bissecção", xr, Epest, iteracao)

    xr, Epest, iteracao = falsaPosicao(f, xl, xu, Eppara)
    exibirResultado("Falsa Posição", xr, Epest, iteracao)

    xr, Epest, iteracao = newtonRaphson(f, df, xi, Eppara)
    exibirResultado("Newton-Raphson", xr, Epest, iteracao)

    xr, Epest, iteracao = secante(f, xl, xu, Eppara)
    exibirResultado("Secante", xr, Epest, iteracao)

    xr, Epest, iteracao = secanteModificado(f, xi, delta, Eppara)
    exibirResultado("Secante Modificado", xr, Epest, iteracao)

print("\nExercício 2")

x0 = 0.5

xr, Epest, iteracao = newtonRaphson(f2, df2, x0, Eppara)
exibirResultado("Newton-Raphson", xr, Epest, iteracao)

xr, Epest, iteracao = bisseccao(f2, 0, 1, Eppara)
exibirResultado("Bissecção", xr, Epest, iteracao)

x = np.linspace(-3, 3, 5000)
plt.figure()
plt.plot(x, fA(x), label="a")
plt.plot(x, fB(x), label="b")
plt.axhline(0)
plt.ylim(-10, 10)
plt.title("Funções a e b")
formatarGrafico()
plt.grid()
plt.legend()

xD = np.linspace(-2, 7, 5000)
xC1 = np.linspace(-0.99, -0.05, 1500)
xC2 = np.linspace(0.05, 7, 3000)
plt.figure()
plt.plot(xC1, fC(xC1), label="c")
corC = plt.gca().lines[-1].get_color()
plt.plot(xC2, fC(xC2), color=corC)
plt.plot(xD, fD(xD), label="d")
plt.axhline(0)
plt.ylim(-10, 10)
plt.title("Funções c e d")
formatarGrafico()
plt.grid()
plt.legend()

x = np.linspace(0.01, 1, 5000)
plt.figure()
plt.plot(x, fE(x), label="e")
plt.plot(x, fF(x), label="f")
plt.axhline(0)
plt.ylim(-70, 10)
plt.title("Funções e e f")
formatarGrafico()
plt.grid()
plt.legend()

x = np.linspace(-3.5, 2, 5000)
plt.figure()
plt.plot(x, fG(x), label="g")
plt.plot(x, fH(x), label="h")
plt.axhline(0)
plt.ylim(-10, 10)
plt.title("Funções g e h")
formatarGrafico()
plt.grid()
plt.legend()

x = np.linspace(0, 1, 5000)
plt.figure()
plt.plot(x, f2(x))
plt.axhline(0)
plt.title("Exercício 2")
formatarGrafico()
plt.grid()

plt.show()
