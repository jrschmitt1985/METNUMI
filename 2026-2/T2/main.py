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
    return 1 + 1 / np.cos(x)**2


def fC(x):
    return np.sqrt(x + 1) - x**(-2)


def dfC(x):
    return 1 / (2*np.sqrt(x + 1)) + 2*x**(-3)


def fD(x):
    return 2**x - 2*x**2 + 1


def dfD(x):
    return 2**x * np.log(2) - 4*x


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


def formatoCientifico(valor):
    return f"{valor:.6e}".replace(".", ",")


def buscaIncremental(f, intervalosBusca, dx):
    intervalos = []

    for inicio, fim in intervalosBusca:
        x = inicio

        while x < fim:
            x2 = min(x + dx, fim)

            try:
                fx = f(x)
                fx2 = f(x2)

                if np.isfinite(fx) and np.isfinite(fx2):
                    if fx == 0:
                        intervalos.append((x, x))
                    elif fx * fx2 < 0:
                        intervalos.append((x, x2))

            except:
                pass

            x = x2

    return intervalos


def menorIntervaloPositivo(intervalos):
    positivos = []

    for xl, xu in intervalos:
        if xu > 0:
            positivos.append((xl, xu))

    if len(positivos) == 0:
        return None

    return min(
        positivos,
        key=lambda intervalo: max(intervalo[0], 0)
    )


def exibirResultado(nomeMetodo, f, xr, Epest, iteracao):
    residuo = abs(f(xr))

    print()
    print(f"{nomeMetodo}:")
    print(f"xr = {xr:.8f}".replace(".", ","))
    print(f"Epest = {formatoCientifico(Epest)}%")
    print(f"|f(xr)| = {formatoCientifico(residuo)}")
    print(f"Iterações = {iteracao}")


def executarMetodos(nome, f, df, intervalo, Eppara, delta):
    xl, xu = intervalo

    if xl == xu:
        print(
            f"Raiz exata encontrada: {xl:.8f}".replace(".", ",")
        )
        return

    print()
    print(f"Menor raiz positiva de {nome}:")

    try:
        xr, Epest, iteracao = bisseccao(
            f,
            xl,
            xu,
            Eppara
        )

        exibirResultado(
            "Bissecção",
            f,
            xr,
            Epest,
            iteracao
        )

    except Exception as erro:
        print()
        print("Bissecção:")
        print("Não convergiu:", erro)

    try:
        xr, Epest, iteracao = falsaPosicao(
            f,
            xl,
            xu,
            Eppara
        )

        exibirResultado(
            "Falsa Posição",
            f,
            xr,
            Epest,
            iteracao
        )

    except Exception as erro:
        print()
        print("Falsa Posição:")
        print("Não convergiu:", erro)

    try:
        xi = (xl + xu) / 2

        xr, Epest, iteracao = newtonRaphson(
            f,
            df,
            xi,
            Eppara
        )

        exibirResultado(
            "Newton-Raphson",
            f,
            xr,
            Epest,
            iteracao
        )

    except Exception as erro:
        print()
        print("Newton-Raphson:")
        print("Não convergiu:", erro)

    try:
        xr, Epest, iteracao = secante(
            f,
            xl,
            xu,
            Eppara
        )

        exibirResultado(
            "Secante",
            f,
            xr,
            Epest,
            iteracao
        )

    except Exception as erro:
        print()
        print("Secante:")
        print("Não convergiu:", erro)

    try:
        xi = (xl + xu) / 2

        xr, Epest, iteracao = secanteModificado(
            f,
            xi,
            delta,
            Eppara
        )

        exibirResultado(
            "Secante Modificado",
            f,
            xr,
            Epest,
            iteracao
        )

    except Exception as erro:
        print()
        print("Secante Modificado:")
        print("Não convergiu:", erro)


def formataGrafico():
    ax = plt.gca()

    ax.xaxis.set_major_formatter(
        FuncFormatter(
            lambda x, pos: f"{x:g}".replace(".", ",")
        )
    )

    ax.yaxis.set_major_formatter(
        FuncFormatter(
            lambda y, pos: f"{y:g}".replace(".", ",")
        )
    )

    plt.axhline(
        0,
        linestyle="--",
        linewidth=1
    )

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.legend()
    plt.tight_layout()


def graficoAB():
    x = np.linspace(-3, 3, 5000)

    with np.errstate(all="ignore"):
        yA = fA(x)
        yB = fB(x)

    yA = np.where(
        np.isfinite(yA),
        yA,
        np.nan
    )

    yB = np.where(
        np.abs(np.cos(x)) > 0.03,
        yB,
        np.nan
    )

    plt.figure(figsize=(10, 6))

    plt.plot(
        x,
        yA,
        label=r"a) $f(x)=x^5-x-1$"
    )

    plt.plot(
        x,
        yB,
        label=r"b) $f(x)=x+\tan(x)$"
    )

    plt.xlim(-3, 3)
    plt.ylim(-10, 10)

    plt.title("Funções a e b")

    formataGrafico()


def graficoCD():
    xD = np.linspace(-2, 7, 5000)

    xC1 = np.linspace(-0.99, -0.05, 1500)
    xC2 = np.linspace(0.05, 7, 3000)

    with np.errstate(all="ignore"):
        yC1 = fC(xC1)
        yC2 = fC(xC2)
        yD = fD(xD)

    plt.figure(figsize=(10, 6))

    plt.plot(
        xC1,
        yC1,
        label=r"c) $f(x)=\sqrt{x+1}-x^{-2}$"
    )

    corC = plt.gca().lines[-1].get_color()

    plt.plot(
        xC2,
        yC2,
        color=corC
    )

    plt.plot(
        xD,
        yD,
        label=r"d) $f(x)=2^x-2x^2+1$"
    )

    plt.xlim(-2, 7)
    plt.ylim(-10, 10)

    plt.title("Funções c e d")

    formataGrafico()


def graficoEF():
    x = np.linspace(0.01, 1, 4000)

    with np.errstate(all="ignore"):
        yE = fE(x)
        yF = fF(x)

    plt.figure(figsize=(10, 6))

    plt.plot(
        x,
        yE,
        label=r"e) $f(x)=\ln(x)-3e^{x+2}$"
    )

    plt.plot(
        x,
        yF,
        label=r"f) $f(x)=\ln(x)+(x+1)^3$"
    )

    plt.xlim(0, 1)
    plt.ylim(-70, 10)

    plt.title("Funções e e f")

    formataGrafico()


def graficoGH():
    x = np.linspace(-3.5, 2, 4000)

    yG = fG(x)
    yH = fH(x)

    plt.figure(figsize=(10, 6))

    plt.plot(
        x,
        yG,
        label=r"g) $f(x)=x^2-\cos(x)$"
    )

    plt.plot(
        x,
        yH,
        label=r"h) $f(x)=e^{-x^2}-x^2-2x+2$"
    )

    plt.xlim(-3.5, 2)
    plt.ylim(-10, 10)

    plt.title("Funções g e h")

    formataGrafico()


def graficoExercicio2():
    x = np.linspace(0, 1, 3000)
    y = f2(x)

    plt.figure(figsize=(10, 6))

    plt.plot(
        x,
        y,
        label=r"$f(x)=e^{-x}-2\sqrt{x}$"
    )

    plt.xlim(0, 1)
    plt.ylim(-2, 1.2)

    plt.title("Exercício 2")

    formataGrafico()


n = 6
Eppara = 0.5 * (10 ** (2 - n))
delta = 0.0000001
dx = 0.01


casos = [
    {
        "nome": "a",
        "titulo": "x⁵ - x - 1 = 0",
        "f": fA,
        "df": dfA,
        "busca": [(-3, 3)],
        "raizes": "busca"
    },
    {
        "nome": "b",
        "titulo": "x + tan(x) = 0",
        "f": fB,
        "df": dfB,
        "busca": [
            (np.pi/2 + 0.01, np.pi - 0.01)
        ],
        "raizes": "infinitas"
    },
    {
        "nome": "c",
        "titulo": "√(x + 1) - x⁻² = 0",
        "f": fC,
        "df": dfC,
        "busca": [
            (-0.999, -0.01),
            (0.01, 5)
        ],
        "raizes": "busca"
    },
    {
        "nome": "d",
        "titulo": "2ˣ - 2x² + 1 = 0",
        "f": fD,
        "df": dfD,
        "busca": [(-5, 10)],
        "raizes": "busca"
    },
    {
        "nome": "e",
        "titulo": "ln(x) - 3e^(x+2) = 0",
        "f": fE,
        "df": dfE,
        "busca": [(0.001, 10)],
        "raizes": "busca"
    },
    {
        "nome": "f",
        "titulo": "ln(x) + (x + 1)³ = 0",
        "f": fF,
        "df": dfF,
        "busca": [(0.001, 5)],
        "raizes": "busca"
    },
    {
        "nome": "g",
        "titulo": "x² - cos(x) = 0",
        "f": fG,
        "df": dfG,
        "busca": [(-3, 3)],
        "raizes": "busca"
    },
    {
        "nome": "h",
        "titulo": "e^(-x²) - x² - 2x + 2 = 0",
        "f": fH,
        "df": dfH,
        "busca": [(-5, 5)],
        "raizes": "busca"
    }
]


print()
print("=" * 50)
print("EXERCÍCIO 1")
print("=" * 50)


for caso in casos:
    nome = caso["nome"]
    f = caso["f"]
    df = caso["df"]

    intervalos = buscaIncremental(
        f,
        caso["busca"],
        dx
    )

    print()
    print("=" * 50)
    print(f"CASO {nome.upper()}")
    print(caso["titulo"])
    print("=" * 50)

    if caso["raizes"] == "infinitas":
        print("Número de raízes reais: infinitas")

    else:
        print(
            "Número de raízes reais detectadas:",
            len(intervalos)
        )

    print("Intervalos com mudança de sinal:")

    if len(intervalos) == 0:
        print("Nenhum intervalo encontrado.")

    else:
        for xl, xu in intervalos:
            resultado = (
                f"xl = {xl:.2f}, xu = {xu:.2f}"
            )

            print(
                resultado.replace(".", ",")
            )

    intervaloPositivo = menorIntervaloPositivo(
        intervalos
    )

    if intervaloPositivo is None:
        print()
        print("Não foi encontrada raiz positiva.")

    else:
        executarMetodos(
            nome,
            f,
            df,
            intervaloPositivo,
            Eppara,
            delta
        )


print()
print("=" * 50)
print("EXERCÍCIO 2")
print("f(x) = e^(-x) - 2√x")
print("=" * 50)


xl2 = 0
xu2 = 1
x02 = 0.5


print()
print("Condição inicial para Newton-Raphson:")
print(f"x0 = {x02:.2f}".replace(".", ","))


xrNewton, EpestNewton, iterNewton = newtonRaphson(
    f2,
    df2,
    x02,
    Eppara
)

xrBisseccao, EpestBisseccao, iterBisseccao = bisseccao(
    f2,
    xl2,
    xu2,
    Eppara
)


exibirResultado(
    "Newton-Raphson",
    f2,
    xrNewton,
    EpestNewton,
    iterNewton
)

exibirResultado(
    "Bissecção",
    f2,
    xrBisseccao,
    EpestBisseccao,
    iterBisseccao
)


print()
print("Comparação:")
print(
    "Newton-Raphson:",
    iterNewton,
    "iterações"
)

print(
    "Bissecção:",
    iterBisseccao,
    "iterações"
)


print()
print("Observação sobre x0 = 0:")

print(
    "x0 = 0 não é conveniente porque f'(x) contém "
    "o termo 1/sqrt(x), que não é definido em x = 0."
)


graficoAB()
graficoCD()
graficoEF()
graficoGH()
graficoExercicio2()

plt.show()