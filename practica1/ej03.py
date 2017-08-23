import numpy as np
from PIL import Image
from sys import argv

im1 = np.asarray(Image.open(argv[1]).convert('L'))
umbral = int(argv[2])
f = np.vectorize(lambda r : 255 if r > umbral else 0)

im2 = np.uint8(f(im1))
j = Image.fromarray(im2)
j.show()
