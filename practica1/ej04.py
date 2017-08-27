'''
Fraccionamiento de los planos de bits: hacer un programa que separe una imagen
en los 8 planos de bits y mostrarlos cada uno por separado

Modo de uso:
  python3 ej04.py <img1>
'''
import numpy as np
import side_by_side
from PIL import Image
from sys import argv

im1 = np.asarray(Image.open(argv[1]).convert('L'))
ims = []
for s in range(8):
    f = np.vectorize(lambda r : 255 if r & (1 << s) > 0 else 0)
    ims.append(np.uint8(f(im1)))

side_by_side.sbys([im1]+ims, ['Original']+['Bit '+str(i) for i in range(8)],
                    argv[2] if len(argv) > 2 else None, 3)  
