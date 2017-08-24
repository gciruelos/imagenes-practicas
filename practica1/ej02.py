'''
Implementar una función que devuelva el negativo de una imagen.

Modo de uso:
  python3 ej02.py <img1>
'''
import numpy as np
from PIL import Image
from sys import argv

im1 = np.asarray(Image.open(argv[1]).convert('L'))

L = 255

f = np.vectorize(lambda r : -r + L)

im2 = np.uint8(f(im1))
j = Image.fromarray(im2)
j.show()
