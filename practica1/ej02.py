from PIL import Image
import numpy as np
from sys import argv
from math import log

im1 = np.asarray(Image.open(argv[1]).convert('L'))

L = 255

f = np.vectorize(lambda r : -r + L)

im2 = np.uint8(f(im1))
j = Image.fromarray(im2)
j.show()
