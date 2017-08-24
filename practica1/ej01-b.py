'''
Producto de una imagen por un escalar.

Modo de uso:
  python3 ej01-b.py <img1> <escalar>
'''
from PIL import Image
import numpy
from sys import argv
im1 = numpy.asarray(Image.open(argv[1]).convert('L'))
f = float(argv[2])
j = Image.fromarray(f*im1)
j.show()
