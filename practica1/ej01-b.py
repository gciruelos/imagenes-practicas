'''
Producto de una imagen por un escalar.

Modo de uso:
  python3 ej01-b.py <img1> <escalar>
'''

from PIL import Image
import numpy
import side_by_side
from sys import argv

im1 = numpy.asarray(Image.open(argv[1]).convert('L'))
f = float(argv[2])
side_by_side.sbys([im1, f*im1], ['Original', 'Por escalar ('+argv[2]+')'], argv[3] if len(argv) > 3 else None)
