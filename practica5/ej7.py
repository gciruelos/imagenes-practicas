#  python practica5/ej7.py <img1> <roberts|prewitt|sobel> <param_gauss> <param_salt_pepper>
import numpy as np
import math
from PIL import Image
from sys import argv
import side_by_side
import convolution
import ej4

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
    r = convolution.scale(np.power(imx+imy, 0.5)) / np.sqrt(2)
    convolution.apply_threshold(r, 150)
    return r


im1 = np.asarray(Image.open(argv[1]).convert('L'))
im3 = ej4.gaussiano(im1, float(argv[3])) 
im5 = ej4.salt_and_pepper(im1, float(argv[4])) 
if argv[2] == "roberts":
    im2 = border_detection(im1, robertsx, robertsy)
    im4 = border_detection(im3, robertsx, robertsy)
    im6 = border_detection(im5, robertsx, robertsy)
elif argv[2] == "prewitt":
    im2 = border_detection(im1, prewittx, prewitty)
    im4 = border_detection(im3, prewittx, prewitty)
    im6 = border_detection(im5, prewittx, prewitty)
elif argv[2] == "sobel":
    im2 = border_detection(im1, sobelx, sobely)
    im4 = border_detection(im3, sobelx, sobely)
    im6 = border_detection(im5, sobelx, sobely)

side_by_side.sbys([im1, im2, im3, im4, im5, im6],
                  ["Original", "Filtro "+argv[2],
                   "Ruido gaussiano: normal(0,"+argv[3]+")", "Filtro "+argv[2],
                   "Ruido salt & pepper: p = "+argv[4], "Filtro "+argv[2]],
                  argv=None if len(argv) <= 5 else argv[5],
                  m=3)
