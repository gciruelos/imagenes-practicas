'''
Fraccionamiento de los planos de bits: hacer un programa que separe una imagen
en los 8 planos de bits y mostrarlos cada uno por separado

Modo de uso:
  python3 ej04.py <img1>
'''
import numpy as np
from PIL import Image
from sys import argv

im1 = np.asarray(Image.open(argv[1]).convert('L'))
for s in range(8):
    f = np.vectorize(lambda r : 255 if r & (1 << s) > 0 else 0)
    im2 = np.uint8(f(im1))
    j = Image.fromarray(im2)
    j.show()
