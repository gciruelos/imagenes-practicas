'''
Implementar una funcion que devuelva el histograma de niveles de gris de una
imagen.

Modo de uso:
  python3 ej05.py <img1>
'''

import numpy as np
from PIL import Image
from sys import argv
import side_by_side

im1 = np.asarray(Image.open(argv[1]).convert('L'))
side_by_side.sbys_histogram([im1], None, argv[2] if len(argv) > 2 else None) 
