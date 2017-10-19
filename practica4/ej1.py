#  python practica4/ej2.py

import cmath
import matplotlib.pyplot as plt
from collections import defaultdict
from math import gcd

def ft1d(N):
    idx_1d = [(n, k) for n in range(N) for k in range(N)]
    ft_1d = [cmath.exp((-1j * 2.0 * cmath.pi * n * k) / N) for (n, k) in idx_1d]
    for n in range(N):
        r = []
        for k in range(N):
            r.append("e^{\\frac{-%d}{%d} \\pi i}" % ((n * k) / gcd(n * k, N), N / gcd(n*k, N)))
        print(' & '.join(r) + " \\\\")

    plt.scatter([z.real for z in ft_1d], [z.imag for z in ft_1d])
    plt.show()

def ft2d(N):
    idx_2d = [(n,k,m,l) for k in range(N) for l in range(N) for n in range(N) for m in range(N)]
    ft_2d = [cmath.exp((-1j * 2.0 * cmath.pi * (n*k + m*l)) / N) for (n,k,m,l) in idx_2d]

    plt.scatter([z.real for z in ft_2d], [z.imag for z in ft_2d])
    plt.show()

ft1d(8)
# ft2d(8)
