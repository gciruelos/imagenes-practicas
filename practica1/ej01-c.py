'''
Compresión del rango dinámico.

Modo de uso:
  python3 ej01-c.py <img1>
'''
import numpy as np
from PIL import Image
from sys import argv
import side_by_side
from math import log

im1 = np.asarray(Image.open(argv[1]).convert('L'))
R = 0
L = 256
for p in np.nditer(im1):
    if p > R:
        R = p
f = np.vectorize(lambda r : (L-1) * log(1 + r) / log(1 + R))
side_by_side.sbys([im1, f(im1)], ['Original', 'Compresion de rango dinamico'], argv[2] if len(argv) > 2 else None)
