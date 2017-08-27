'''
Implementar una función que aplique un umbral a una imagen, devolviendo una imagen binaria.

Modo de uso:
  python3 ej03.py <img1> <umbral>
'''
import numpy as np
from PIL import Image
from sys import argv
import side_by_side

im1 = np.asarray(Image.open(argv[1]).convert('L'))
umbral = int(argv[2])
f = np.vectorize(lambda r : 255 if r > umbral else 0)

side_by_side.sbys([im1, np.uint8(f(im1))],
                    ['Original', 'Umbral ('+argv[2]+')'], argv[3] if len(argv) > 3 else None)
