#  python practica5/ej4.py <img> <gauss|rayleigh> <param>
import numpy as np
import math
from PIL import Image
from sys import argv
import side_by_side
import ej3

def gaussiano(img, sigma):
    mu = 0

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

def rayleigh(img, a):
    b = 1

    K1, K2 = img.shape
    r = np.zeros(img.shape, dtype=np.float)
    maximum = 0.0
    minimum = 0.0
    for k1 in range(K1):
        for k2 in range(K2):
            x = float(img[k1,k2])
            rayleigh = a + np.sqrt(-1 * b * np.log(1 - np.random.uniform(0, 1)))
            x *= rayleigh
            r[k1,k2] = x
    return r

def salt_and_pepper(img, p):
    a = float(argv[3])
    b = 1

    K1, K2 = img.shape
    r = np.zeros(img.shape, dtype=np.float)
    for k1 in range(K1):
        for k2 in range(K2):
            if np.random.uniform(0, 1) < p:
                r[k1,k2] = 255 if np.random.uniform(0,1) < 0.5 else 0
            else:
                r[k1,k2] = img[k1,k2]
    return r

if __name__ == "__main__":
    if argv[2] == "gauss":
        im1 = np.asarray(Image.open(argv[1]).convert('L'))
        im2 = gaussiano(im1, float(argv[3]))
    elif argv[2] == "rayleigh":
        im1 = np.asarray(Image.open(argv[1]).convert('L'))
        im2 = rayleigh(im1, float(argv[3]))

    print(im1)
    print(im2)
    im3 = ej3.suavizadof(im2)
    im4 = ej3.realce_de_bordes(im2)

    side_by_side.sbys([im1, im2, im3, im4],
                      ["Original", "Ruido "+("gaussiano: normal(0,"+argv[3]+")" if argv[2] == "gauss"
                                             else "rayleigh: "+argv[3]), "Suavizado", "Unsharp masking"],
                      argv=None if len(argv) <= 4 else argv[4],
                      m=2)
