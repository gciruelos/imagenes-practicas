#  python practica5/ej4.py <img> <gauss|rayleigh> <param>
import numpy as np
import math
from PIL import Image
from sys import argv
import side_by_side

def gaussiano(img):
    mu = 0
    sigma = float(argv[3])

    K1, K2 = img.shape
    r = np.zeros(img.shape, dtype=np.uint8)
    maximum = 0.0
    minimum = 0.0
    for k1 in range(K1):
        for k2 in range(K2):
            x = float(img[k1,k2])
            x += np.random.normal(mu, sigma)
            if x < 0: x = 0
            elif x > 255: x = 255
            r[k1,k2] = x
    return r

def rayleigh(img):
    a = float(argv[3])
    b = 1

    K1, K2 = img.shape
    r = np.zeros(img.shape, dtype=np.uint8)
    maximum = 0.0
    minimum = 0.0
    for k1 in range(K1):
        for k2 in range(K2):
            x = float(img[k1,k2])
            rayleigh = a + np.sqrt(-1 * b * np.log(1 - np.random.uniform(0, 1)))
            x *= rayleigh
            if x < 0: x = 0
            elif x > 255: x = 255
            r[k1,k2] = x
    return r
    

if argv[2] == "gauss":
    im1 = np.asarray(Image.open(argv[1]).convert('L'))
    im2 = gaussiano(im1)
elif argv[2] == "rayleigh":
    im1 = np.asarray(Image.open(argv[1]).convert('L'))
    im2 = rayleigh(im1)

print(im1)
print(im2)

side_by_side.sbys([im1, im2])
