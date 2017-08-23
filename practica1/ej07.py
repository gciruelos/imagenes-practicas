'''
Implementar una funci ́on que resuelva la ecualizacion del histograma.
'''

import numpy as np
from PIL import Image
from sys import argv
import matplotlib.pyplot as plt
import math

L = 256

def histogram(img):
    histogram = [0] * 256
    nm = 0
    for p in np.nditer(img):
        histogram[p] += 1
        nm += 1

    for i in range(256):
        histogram[i] = float(histogram[i]) / nm

    accum = [0] * 256
    for i in range(256):
        for j in range(i):
            accum[i] += histogram[j]
            if accum[i] > 1.0: accum[i] = 1.0
    return histogram, accum

def side_by_side(ims):
    imgs = list(map(Image.fromarray, ims))
    n = len(imgs)
    whs = list(map(lambda x: x.size, imgs))

    histograms = list(map(histogram, ims))
    f, axs = plt.subplots(3, n)
    for i in range(n):
        axs[0][i].imshow(imgs[i], cmap='gray', vmin=0, vmax=255)
    for i in range(n):
        axs[1][i].plot(range(L), histograms[i][0])
    for i in range(n):
        axs[2][i].plot(range(L), histograms[i][1])
    plt.show()

im1 = np.asarray(Image.open(argv[1]).convert('L'))

# Ejercicio 6
def naive_hist(im):
    s_min = 255
    for p in np.nditer(im):
        if p < s_min: s_min = p
    def scale(r):
        r = float(r) / 255
        smin = float(s_min) / 255
        return float(L - 1) * (r - smin) / (1 - smin) + 0.5
    f = np.vectorize(scale)
    return f(im)

# Ejercicios 7 y 8
def uniform_hist(im):
    hist, acc = histogram(im)
    def w_dot(r):
        w = acc[r]
        for n in range(L):
            # w^tilde_n = n / L
            if float(n+1) / L   - w >= 0:
                return n
        # print(L, n, w, r)
    f = np.vectorize(w_dot)
    return f(im)

# Ejercicio 9
def normal_hist(im):
    mu = float(L) / 2.0
    sigma = math.sqrt(float(L) / 4.0)
    hist, acc = histogram(im)
    def prob_normal(n):
        n = float(n)
        return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(
                                    -0.5 * math.pow((n - mu) / sigma, 2))
    def w_dot(r):
        w = acc[r]
        probs = [prob_normal(i) for i in range(L)]
        accum_max = sum(probs)
        for n in range(L):
            if sum(probs[:n+1]) / accum_max - w >= 0:
                return n
        # print(L, n, sum(probs[:n]) / accum_max , w, r)
    f = np.vectorize(w_dot)
    return f(im)


im2 = np.uint8(uniform_hist(im1))
im3 = np.uint8(uniform_hist(uniform_hist(im1)))
side_by_side([im1, im2, im3])

im4 = np.uint8(naive_hist(im1))
side_by_side([im1, im4])

im5 = np.uint8(normal_hist(im1))
side_by_side([im1, im5])


''' 
Ejercicio 9: LIM (capitulo 7)
N(L/2, L/4) ~ N(128, 64), f(x) = ...

  I = I / max(I)
  h_I = histograma(I)
  h_Iacum = histograma_acumulado(I)

  x = 0:255
  p_x = 1 / (64 sqrt(2 pi))  *  exp(-0.5 ((x-128) / 64)^2)

'''
