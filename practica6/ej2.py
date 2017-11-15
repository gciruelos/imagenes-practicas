import side_by_side
import convolution
import numpy as np
from PIL import Image
from sys import argv
import math

LAPLACIAN_THRESHOLD = 20
VARIANZA_THRESHOLD = 2.0

laplaciano = np.zeros((3,3), dtype=np.float);
laplaciano[1,1] = -4
laplaciano[0,1] = 1
laplaciano[2,1] = 1
laplaciano[1,0] = 1
laplaciano[1,2] = 1

def mediana_difs(im1):
    l = []
    K1, K2 = im1.shape
    for k1 in range(1,K1-1):
        for k2 in range(1, K2-1):
            indices = [((k1-1, k2-1), (k1+1, k2+1)),
                       ((k1, k2-1), (k1, k2+1)),
                       ((k1-1, k2), (k1+1, k2)),
                       ((k1+1, k2-1), (k1-1, k2+1))]
            m = 0
            for i1, i2 in indices:
                p1 = im1[i1[0], i1[1]]
                p2 = im1[i2[0], i2[1]]
                if abs(p1-p2) > m: m = abs(p1-p2)
            l.append(m)
    r = sorted(l)[len(l) // 2]
    return r

def ej_a(im1):
    K1, K2 = im1.shape
    im2= convolution.convolution(im1, laplaciano)
    r = np.zeros(im1.shape, dtype=np.float)
    maximum = 0.0
    minimum = 0.0
    median = mediana_difs(im2) * 2.0
    for k1 in range(1,K1-1):
        for k2 in range(1, K2-1):
            indices = [((k1-1, k2-1), (k1+1, k2+1)),
                       ((k1, k2-1), (k1, k2+1)),
                       ((k1-1, k2), (k1+1, k2)),
                       ((k1+1, k2-1), (k1-1, k2+1))]
            found = False
            for i1, i2 in indices:
                p1 = im2[i1[0], i1[1]]
                p2 = im2[i2[0], i2[1]]
                if p1 * p2 < 0 and abs(p1 - p2) > median:
                    found = True
                    break
            r[k1, k2] = 255 if found else 0
    return r

def media_local(img, m, i_, j_):
    k1, k2 = img.shape
    todos = []
    for i in range(i_ - m, i_ + m + 1):
        for j in range(j_ - m, j_ + m + 1):
            if i < 0 or i >= k1:
                continue
            elif j < 0 or j >= k2:
                continue
            else:
                todos.append(img[i, j]) 
    return sum(todos) / len(todos)

def varianza_local(img, m, i_, j_):
    k1, k2 = img.shape
    todos = []
    for i in range(i_ - m, i_ + m + 1):
        for j in range(j_ - m, j_ + m + 1):
            if i < 0 or i >= k1:
                continue
            elif j < 0 or j >= k2:
                continue
            else:
                todos.append(math.pow(img[i_, j_] - media_local(img, m, i, j), 2)) 
    return math.sqrt(sum(todos)) / len(todos)


    

def ej_b(im1):
    K1, K2 = im1.shape
    im2= convolution.convolution(im1, laplaciano)
    r = np.zeros(im1.shape, dtype=np.float)
    maximum = 0.0
    minimum = 0.0
    mediana = mediana_difs(im2) * 2.0
    for k1 in range(1,K1-1):
        for k2 in range(1, K2-1):
            indices = [((k1-1, k2-1), (k1+1, k2+1)),
                       ((k1, k2-1), (k1, k2+1)),
                       ((k1-1, k2), (k1+1, k2)),
                       ((k1+1, k2-1), (k1-1, k2+1))]
            found = False
            varianza = varianza_local(im2, 2, k1, k2)
            if varianza < VARIANZA_THRESHOLD: continue
            for i1, i2 in indices:
                p1 = im2[i1[0], i1[1]]
                p2 = im2[i2[0], i2[1]]
                if p1 * p2 < 0 and abs(p1 - p2) >= mediana:
                    found = True
                    break
            r[k1, k2] = 255 if found else 0
    return r


def ej_c(im1):
    gaussian = np.ones((5,5), dtype=np.float);
    gaussian[:,:] = [
        [1,4,7,4,1],
        [4,16,26,16,4],
        [7,26,41,26,7],
        [4,16,26,16,4],
        [1,4,7,4,1]]
    gaussian[:,:] *= 1./273;
    im2 = convolution.convolution(im1, gaussian)
    return ej_a(im2)


im1 = np.asarray(Image.open(argv[1]).convert('L'))
fname = "???"
filtro = argv[2]
if filtro == "a":
    im2 = ej_a(im1)
    fname = "Metodo del Laplaciano"
elif filtro == "b":
    im2 = ej_b(im1)
    fname = "Metodo del Laplaciano con thershold de varianza"
elif filtro == "c":
    im2 = ej_c(im1)
    fname = "Metodo del Laplaciano del Gaussiano"
side_by_side.sbys([im1, im2],
                  ["Original", fname],
                  argv=None if len(argv) <= 3 else argv[3])
