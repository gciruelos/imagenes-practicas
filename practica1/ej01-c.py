import numpy as np
from PIL import Image
from sys import argv
from math import log
im1 = np.asarray(Image.open(argv[1]).convert('L'))
R = 0
L = 256
for p in np.nditer(im1):
    if p > R:
        R = p

f = np.vectorize(lambda r : (L-1) * log(1 + r) / log(1 + R))
j = Image.fromarray(f(im1))
j.show()
