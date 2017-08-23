'''
Implementar una funcion que devuelva el histograma de niveles de gris de una
imagen.
'''

import numpy as np
from PIL import Image
from sys import argv
import matplotlib.pyplot as plt

im1 = np.asarray(Image.open(argv[1]).convert('L'))

histogram = [0] * 256
nm = 0
for p in np.nditer(im1):
    histogram[p] += 1
    nm += 1

for i in range(256):
    histogram[i] = float(histogram[i]) / nm

plt.plot(list(range(256)), histogram)
plt.show()
