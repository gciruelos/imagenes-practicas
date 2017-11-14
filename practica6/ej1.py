#  python practica6/ej1.py <img> <output_dir?>
import numpy as np
import math
from PIL import Image
from sys import argv

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
    r = np.zeros(img.shape, dtype=np.uint8)
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
    K1, K2 = img.shape
    r = np.zeros(img.shape, dtype=np.uint8)
    for k1 in range(K1):
        for k2 in range(K2):
            if np.random.uniform(0, 1) < p:
                r[k1,k2] = 255 if np.random.uniform(0,1) < 0.5 else 0
            else:
                r[k1,k2] = img[k1,k2]
    return r

if __name__ == "__main__":
    filename = argv[1] if argv[1][-1] != '/' else argv[1][:-1]
    odir = '.' if len(argv) < 2 else argv[2]
    filename_no_extension = filename.split('/')[-1].split('.')[0]
    fne = filename_no_extension
    original = np.asarray(Image.open(argv[1]).convert('L'))
    gauss1 = gaussiano(original, 10)
    gauss2 = gaussiano(original, 50)
    rayleigh = rayleigh(original, 1.5)
    saltpepper = salt_and_pepper(original, 0.1)
    Image.fromarray(original).save(odir+'/'+fne+"-original.png")
    Image.fromarray(gauss1).save(odir+'/'+fne+"-gauss10.png")
    Image.fromarray(gauss2).save(odir+'/'+fne+"-gauss50.png")
    Image.fromarray(rayleigh).save(odir+'/'+fne+"-rayleigh15.png")
    Image.fromarray(saltpepper).save(odir+'/'+fne+"-saltpepper10.png")

