#  python practica5/ej3.py <img1> <a|b>
import numpy as np
import math
from PIL import Image
from sys import argv
import side_by_side
import convolution


# https://homepages.inf.ed.ac.uk/rbf/HIPR2/gsmooth.htm
suavizado = np.zeros((5,5), dtype=np.float)
suavizado[:,:] = [[1,4,7,4,1],
                  [4,16,26,16,4],
                  [7,26,41,26,7],
                  [4,16,26,16,4],
                  [1,4,7,4,1]]
suavizado[:,:] *= 1./273

# https://homepages.inf.ed.ac.uk/rbf/HIPR2/unsharp.htm
unsharp = np.zeros((3,3), dtype=np.float)
unsharp[:,:] = [[-1,-2,-1],
                [-2,12,-2],
                [-1,-2,-1]]
unsharp[:,:] *= 1./16

def suavizadof(img):
    return convolution.convolution(img, suavizado)

def realce_de_bordes(im1):
    im2 = convolution.convolution(im1, unsharp)

    im2 += im1
    return im2

if __name__ == "__main__":
    if argv[2] == "a":
        im1 = np.asarray(Image.open(argv[1]).convert('L'))
        im2 = suavizadof(im1)
    elif argv[2] == "b":
        im1 = np.asarray(Image.open(argv[1]).convert('L'))
        im2 = realce_de_bordes(im1)
    elif argv[2] == "c":
        im1 = np.asarray(Image.open(argv[1]).convert('L'))
        im5 = convolution.convolution(im1, suavizado)
        THRESHOLD = 200
        im2 = convolution.convolution(im5, unsharp)

        idx = im2[:,:] > THRESHOLD
        im2[idx] = THRESHOLD

        im2 = im2.astype(np.uint16)
        im2 += im1
        m = np.amax(im2)
        im3 = im2 * 255.0 / m
        im2 = im3.astype(np.uint8)
        side_by_side.sbys([im1, im5, im2])
        exit(0)

    print(im1)
    print(im2)

    side_by_side.sbys([im1, im2], ["Original", "Suavizado" if argv[2] == "a" else "Unsharp masking"],
                      argv=None if len(argv) <= 3 else argv[3])
