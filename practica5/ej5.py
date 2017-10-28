#  python practica5/ej5.py <img> <param_gauss> <param_salt_pepper>
import numpy as np
import math
from PIL import Image
from sys import argv
import side_by_side
import ej4


def mediana(img):
    r = np.zeros(img.shape, dtype=np.uint8)
    K1, K2 = img.shape
    for k1 in range(K1):
        for k2 in range(K2):
            r[k1, k2] = img[k1,k2]
            if k1 == 0 or k1 == K1 - 1 or k2 == 0 or k2 == K2 - 1:
                continue
            r[k1,k2] = sorted([img[k1-1, k2-1], img[k1-1, k2], img[k1-1, k2+1],
                               img[k1, k2-1], img[k1, k2], img[k1, k2+1],
                               img[k1+1, k2-1], img[k1+1, k2], img[k1+1, k2+1]])[4]
    return r

im1 = np.asarray(Image.open(argv[1]).convert('L'))
im2 = mediana(im1)
im3 = ej4.gaussiano(im1, float(argv[2])) 
im4 = mediana(im3)
im5 = ej4.salt_and_pepper(im1, float(argv[3])) 
im6 = mediana(im5)

side_by_side.sbys([im1, im2, im3, im4, im5, im6],
                  ["Original", "Mediana",
                   "Ruido gaussiano: normal(0,"+argv[2]+")", "Mediana",
                   "Ruido salt & pepper: p = "+argv[3], "Mediana"],
                  argv=None if len(argv) <= 4 else argv[4],
                  m=3)
