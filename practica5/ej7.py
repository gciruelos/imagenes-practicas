#  python practica5/ej7.py <img1> <roberts|prewitt|sobel> <x|y>
import numpy as np
import math
from PIL import Image
from sys import argv
import side_by_side
import convolution

robertsx = np.zeros((2,2), dtype=np.float)
robertsx[:,:] = [[1,0],
                 [0,-1]]
robertsy = np.zeros((2,2), dtype=np.float)
robertsy[:,:] = [[0,1],
                 [-1,0]]

prewittx = np.zeros((3,3), dtype=np.float)
prewittx[:,:] = [[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]]
prewitty = np.zeros((3,3), dtype=np.float)
prewitty[:,:] = [[1, 1, 1],
                 [0, 0, 0],
                 [-1, -1, -1]]

sobelx = np.zeros((3,3), dtype=np.float)
sobelx[:,:] = [[1, 0, -1],
               [2, 0, -2],
               [1, 0, -1]]
sobely = np.zeros((3,3), dtype=np.float)
sobely[:,:] = [[1, 2, 1],
               [0, 0, 0],
               [-1, -2, -1]]


def border_detection(img, kernelx, kernely):
    imx = convolution.convolution(img, kernelx)
    imx = imx.astype(np.float)
    imy = convolution.convolution(img, kernely)
    imy = imy.astype(np.float)

    imx = np.power(imx, 2)
    imy = np.power(imy, 2)
    r = convolution.scale(np.power(imx+imy, 0.5))
    convolution.apply_threshold(r, 150)
    return r

if argv[2] == "roberts":
    im1 = np.asarray(Image.open(argv[1]).convert('L'))
    im2 = border_detection(im1, robertsx, robertsy)
elif argv[2] == "prewitt":
    im1 = np.asarray(Image.open(argv[1]).convert('L'))
    im2 = border_detection(im1, prewittx, prewitty)
elif argv[2] == "sobel":
    im1 = np.asarray(Image.open(argv[1]).convert('L'))
    im2 = border_detection(im1, sobelx, sobely)

print(im1)
print(im2)

side_by_side.sbys([im1, im2])
