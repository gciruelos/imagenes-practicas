#  python practica4/ej4.py <img1> <img2>
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


im1 = np.asarray(Image.open(argv[1]).convert('L'))
im2 = np.asarray(Image.open(argv[2]).convert('L'))
dft_im1 = fft2d(im1)
dft_im2 = fft2d(im2)
im1mod, im1phase = mod_and_phase(dft_im1)
im2mod, im2phase = mod_and_phase(dft_im2)

im3 = ifft2d(from_mod_and_phase(im1mod, im2phase))
im4 = ifft2d(from_mod_and_phase(im2mod, im1phase))

print(im1mod)

side_by_side.sbysfourier([im1, im1mod, im1phase])
side_by_side.sbysfourier([im2, im2mod, im2phase])
side_by_side.sbys3([im1, im2, im3], ['im1', 'im2', 'im1mod, im2phase'])
side_by_side.sbys3([im1, im2, im4], ['im1', 'im2', 'im2mod, im1phase'])
