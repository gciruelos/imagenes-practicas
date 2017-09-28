'''
'''
import numpy as np
import cmath
import math
from PIL import Image
from sys import argv
import side_by_side

L = 255



def dft2d(img):
    N1, N2 = img.shape
    r = np.zeros(img.shape, dtype=np.complex64)
    pi2N1 = cmath.pi * 2.0 / N1
    pi2N2 = cmath.pi * 2.0 / N2

    n1ft = np.zeros((N1,N1), dtype=np.complex64)
    n2ft = np.zeros((N2,N2), dtype=np.complex64)
    for n1 in range(N1):
        for k1 in range(n1,N1):
            n1ft[n1,k1] = cmath.exp(-1j * pi2N1 * n1 * k1)
            n1ft[k1,n1] = cmath.exp(-1j * pi2N1 * n1 * k1)
    for n2 in range(N2):
        for k2 in range(N2):
            n2ft[n2,k2] = cmath.exp(-1j * pi2N2 * n2 * k2)
            n2ft[k2,n2] = cmath.exp(-1j * pi2N2 * n2 * k2)

    for k1 in range(N1):
        for k2 in range(N2):
            # img[n1, n2] * cmath.exp(-1j * (pi2N1 * k1 * n1 + pi2N2 * k2 * n2))
            # = img[n1, n2] * cmath.exp(-1j *pi2N1*k1*n1) * cmath.exp(-1j *pi2N2*k2*n2)
            # = img[n1, n2] * cmath.exp(-1j *pi2N1*n1)^k1 * cmath.exp(-1j *pi2N2*n2)^k2
            r[k1, k2] += sum([img[n1, n2] * n1ft[n1,k1] * n2ft[n2,k2] for n1 in range(N1) for n2 in range(N2)])
        print(k1)
    # for n_1 in range(
    return r

def fft2d(img):
    return np.fft.fft2(img)

def mod_and_phase(ft):
    N1, N2 = ft.shape
    mod = np.zeros(ft.shape, dtype=np.float)
    phase = np.zeros(ft.shape, dtype=np.float)
    for k1 in range(N1):
        for k2 in range(N2):
            mod[k1, k2], phase[k1, k2] = cmath.polar(ft[k1, k2]) 
    return mod, phase


im1 = np.asarray(Image.open(argv[1]).convert('L'))
dft_im1 = fft2d(im1)
im2, im3 = mod_and_phase(dft_im1)

print(im2)
print(im3)

side_by_side.sbysfourier([im1, im2, im3])
