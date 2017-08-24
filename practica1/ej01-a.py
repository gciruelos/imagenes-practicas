'''
Suma, resta y producto de imágenes.

Modo de uso:
  python3 ej01-a.py <img1> <img2>
'''
from PIL import Image
import numpy
from sys import argv
im1 = numpy.asarray(Image.open(argv[1]).convert('L'))
im2 = numpy.asarray(Image.open(argv[2]).convert('L'))
if argv[3] == 'suma':
    j = Image.fromarray(im1+im2)
    j.show()
if argv[3] == 'resta':
    j = Image.fromarray(im1-im2)
    j.show()
if argv[3] == 'producto':
    j = Image.fromarray(im1*im2)
    j.show()
