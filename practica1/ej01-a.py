'''
Suma, resta y producto de imágenes.

Modo de uso:
  python3 ej01-a.py <img1> <img2> <operacion>
'''
from PIL import Image
import numpy
import side_by_side
from sys import argv

im1 = numpy.asarray(Image.open(argv[1]).convert('L'))
im2 = numpy.asarray(Image.open(argv[2]).convert('L'))
if argv[3] == 'suma':
    side_by_side.sbys([im1, im2, im1 + numpy.minimum(255 - im1, im2)],
        ['Imagen 1', 'Imagen 2', 'Suma'],
        argv[4] if len(argv) > 4 else None)
if argv[3] == 'resta':
    side_by_side.sbys([im1, im2, im1- numpy.minimum(im1, im2)],
        ['Imagen 1', 'Imagen 2', 'Resta'],
        argv[4] if len(argv) > 4 else None)
if argv[3] == 'producto':
    side_by_side.sbys([im1, im2, im1 * numpy.minimum(255 / im1, im2)],
        ['Imagen 1', 'Imagen 2', 'Producto'],
        argv[4] if len(argv) > 4 else None)
