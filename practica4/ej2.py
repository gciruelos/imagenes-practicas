#  python practica4/ej2.py
senial = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

import cmath
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def complexmod(x, n = 2):
    return cmath.polar(x)[0]

def dft(f):
    N = len(f)
    r = [1.0 / math.sqrt(N) * sum(f[n] * cmath.exp((-1j * 2.0 * cmath.pi * n * k) / N) for n in range(N)) for k in range(N)]
    return r

def idft(f):
    N = len(f)
    r = [1.0 / math.sqrt(N) * sum(f[k] * cmath.exp((1j * 2.0 * cmath.pi * n * k) / N) for k in range(N)) for n in range(N)]
    return list(map(complexmod, r))

def filtro_elimino_bajo(f):
    bajos = (len(f) // 3)
    return [0 + 0j for _ in range(bajos)]+f[bajos:]

def filtro_elimino_alto(f):
    altos = (len(f) // 3)
    return f[:len(f)-altos]+[0 + 0j for _ in range(altos)]

def filtro_elimino_medio(f):
    medios = (len(f) // 3)
    return f[0:medios] + [0 + 0j for _ in range(medios)] + f[2*medios:]

d = dft(senial)

plt.plot(senial)
plt.savefig("informe-imgs/ej2-senial.pdf")

def graficar(f, s):
    pasa = f(d)

    gs = gridspec.GridSpec(4, 1)
    plt.subplot(gs[0]).plot(senial)
    plt.subplot(gs[1]).plot(list(map(complexmod, d)))
    plt.subplot(gs[2]).plot(list(map(complexmod, pasa)))
    plt.subplot(gs[3]).plot(idft(pasa))
    plt.savefig("informe-imgs/ej2-"+s+".pdf", bbox_inches='tight')


graficar(filtro_elimino_alto, "elimino-alto")
graficar(filtro_elimino_bajo, "elimino-bajo")
graficar(filtro_elimino_medio, "elimino-medio")

# print(d)
# print(idft(d))

