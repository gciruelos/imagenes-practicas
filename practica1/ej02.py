'''
Implementar una función que devuelva el negativo de una imagen.

Modo de uso:
  python3 ej02.py <img1>
'''
import numpy as np
from PIL import Image
from sys import argv
import side_by_side


im1 = np.asarray(Image.open(argv[1]).convert('L'))

L = 255

f = np.vectorize(lambda r : -r + L)

im2 = np.uint8(f(im1))
side_by_side.sbys([im1, im2], ['Original', 'Negativo'], argv[2] if len(argv) > 2 else None)
