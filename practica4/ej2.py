#  python practica4/ej2.py
senial = [1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0]

import cmath
import math

def roundcomplex(x, n = 2):
    return round(x.real, n) + round(x.imag, n) * 1j

def dft(f):
    N = len(f)
    r = [1.0 / math.sqrt(N) * sum(f[n] * cmath.exp((-1j * 2.0 * cmath.pi * n * k) / N) for n in range(N)) for k in range(N)]
    return list(map(roundcomplex, r))

def idft(f):
    N = len(f)
    r = [1.0 / math.sqrt(N) * sum(f[k] * cmath.exp((1j * 2.0 * cmath.pi * n * k) / N) for k in range(N)) for n in range(N)]
    return list(map(roundcomplex, r))

def filtro_elimino_bajo(f):
    bajos = (len(f) // 3)
    return [0 + 0j for _ in range(bajos)]+f[bajos:]

def filtro_elimino_alto(f):
    altos = (len(f) // 3)
    return f[:len(f)-altos]+[0 + 0j for _ in range(altos)]

d = dft(senial)
eb = filtro_elimino_bajo(d)
ea = filtro_elimino_alto(d)

print(d)
print(idft(d))
print()

print(eb)
print(idft(eb))
print()

print(ea)
print(idft(ea))
# print(d)
# print(idft(d))

