#  python practica4/ej5.py <img1> <img2>

import numpy as np
import cmath
import math
from PIL import Image
from sys import argv
import side_by_side


def fft2d(img):
    return np.fft.fft2(np.vectorize(lambda x: x / 255)(img))

def ifft2d(img):
    return np.vectorize(lambda x: int(x.real * 255))(np.fft.ifft2(img))

def mod_and_phase(ft):
    N1, N2 = ft.shape
    mod = np.zeros(ft.shape, dtype=np.float)
    phase = np.zeros(ft.shape, dtype=np.float)
    for k1 in range(N1):
        for k2 in range(N2):
            mod[k1, k2], phase[k1, k2] = cmath.polar(ft[k1, k2]) 
    return mod, phase

def from_mod_and_phase(mod, phase):
    N1, N2 = mod.shape
    total = np.zeros(mod.shape, dtype=np.complex64)
    for k1 in range(N1):
        for k2 in range(N2):
            total[k1, k2] = cmath.rect(mod[k1, k2], phase[k1, k2])
    return total

# Lena
im1 = np.asarray(Image.open(argv[1]).convert('L'))
dft_im1 = fft2d(im1)
im1mod, im1phase = mod_and_phase(dft_im1)

# Lineas
im2 = np.asarray(Image.open(argv[2]).convert('L'))
dft_im2 = fft2d(im2)
im2mod, im2phase = mod_and_phase(dft_im2)

# Suma
suma = im1 + np.minimum(255 - im1, im2)
dft_suma = fft2d(suma)
sumamod, sumaphase = mod_and_phase(dft_suma)

res = ifft2d(from_mod_and_phase(sumamod -im2mod + im1mod, sumaphase ))
dft_res = fft2d(res)
resmod, resphase = mod_and_phase(dft_res)

if len(argv) < 4:
    side_by_side.sbysfourier([im1, im1mod, im1phase]) 
    side_by_side.sbysfourier([im2, im2mod, im2phase]) 
    side_by_side.sbysfourier([suma, sumamod, sumaphase])
    side_by_side.sbysfourier([res, resmod, resphase]) 
else:
    side_by_side.sbysfourier([im1, im1mod, im1phase], argv="informe-imgs/ej5-lena.pdf") 
    side_by_side.sbysfourier([im2, im2mod, im2phase], argv="informe-imgs/ej5-lineas.pdf") 
    side_by_side.sbysfourier([suma, sumamod, sumaphase], argv="informe-imgs/ej5-suma.pdf") 
    side_by_side.sbysfourier([res, resmod, resphase], argv="informe-imgs/ej5-res.pdf") 
