'''
6. Examinando el histograma del ejercicio anterior, implementar una función que
   devuelva una imagen que tenga aumento del contraste.
7. Implementar una función que resuelva la ecualización del histograma.
8. Aplicar la ecualización del histograma por segunda vez a la misma imagen.
   Observar el resultado y dar una explicación de lo sucedido.
9. Implementar la especificación del histograma para obtener una distribución
   normal con media L/2 y desvı́o L/4. (...).
10. Implementar un algoritmo que dada una imagen de entrada devuelva diferentes
    imágenes correspondientes a diferentes parámetros en la modificaciòn de
    histogramas.
'''

import numpy as np
from PIL import Image
from sys import argv
import side_by_side
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math

L = 256
im1 = np.asarray(Image.open(argv[1]).convert('L'))

def histogram(img):
    return side_by_side.histogram(img)

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
        return int(w * L - 0.5)
        # # Es mas lento hacer:
        # for n in range(L):
        #     if n+1 >= int(w * L + 0.4999):
        #         if n != n_: print (w, L, w*L, n, n_)
        #         return n
        # print(L, n, w, r)
    f = np.vectorize(w_dot)
    return f(im)

# Ejercicio 9
def normal_hist(im):
    mu = float(L) / 2.0
    sigma = float(L) / 4.0
    hist, acc = histogram(im)
    def prob_normal(n):
        n = float(n)
        return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(
                                    -0.5 * math.pow((n - mu) / sigma, 2))
    probs = [prob_normal(i) for i in range(L)]
    accums = [sum(probs[:i+1]) for i in range(L)]
    accum_max = sum(probs)
    def w_dot(r):
        w = acc[r]
        for n in range(L):
            if accums[n] / accum_max - w >= 0:
                return n
        # print(L, n, sum(probs[:n]) / accum_max , w, r)
    f = np.vectorize(w_dot)
    return f(im)

# Ecualizacion con lambda
def lambda_hist(im, lam = 2.0):
    hist, acc = histogram(im)
    def w_dot(r):
        w = acc[r]
        return float(int(w * L - 0.5)) / (1.0 + lam) + lam * float(r) / (1.0 + lam)
    f = np.vectorize(w_dot)
    return f(im)



im4 = np.uint8(naive_hist(im1))
side_by_side.sbys_histogram([im1, im4], ['original', 'naive equalization'])

im2 = np.uint8(uniform_hist(im1))
im3 = np.uint8(uniform_hist(uniform_hist(im1)))
side_by_side.sbys_histogram([im1, im2, im3],
							['original', 'uniform equalization', 'uniform^2 equalization'])

im5 = np.uint8(normal_hist(im1))
side_by_side.sbys_histogram([im1, im5], ['original', 'normal equalization'])

im6 = np.uint8(lambda_hist(im1, 2))
im7 = np.uint8(lambda_hist(im1, 5))
im8 = np.uint8(lambda_hist(im1, 10))
side_by_side.sbys_histogram([im1, im6, im7, im8],
							['original', 'lambda = 2', 'lambda = 5', 'lambda = 10'])

side_by_side.sbys_histogram([im1, im2, im5, im6],
             ['original', 'uniform equalization', 'normal equalization', 'lambda = 2'])

''' 
Ejercicio 9: LIM (capitulo 7)
'''
