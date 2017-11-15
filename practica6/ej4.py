
import side_by_side
import convolution
import numpy as np
from PIL import Image
from sys import argv
import math

def gaussiano(im):
    gaussian = np.ones((5,5), dtype=np.float);
    gaussian[:,:] = [
        [1,4,7,4,1],
        [4,16,26,16,4],
        [7,26,41,26,7],
        [4,16,26,16,4],
        [1,4,7,4,1]]
    gaussian[:,:] *= 1./273;

    return convolution.convolution(im, gaussian)

def edge_detection(im, kernel):
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

        r = np.power(np.power(imx, 2)+np.power(imy, 2), 0.5) / np.sqrt(2.0)
        t = np.arctan(imy / (imx + 0.00001))
        return r, t  

    if kernel == "roberts":
        return border_detection(im1, robertsx, robertsy)
    elif kernel == "prewitt":
        return border_detection(im1, prewittx, prewitty)
    elif kernel == "sobel":
        return border_detection(im1, sobelx, sobely)

def supresion_de_no_maximos(jo, jm):
    jn = np.zeros(jm.shape, dtype=np.float)
    k1, k2 = jm.shape
    for i in range(1, k1-1):
        for j in range(1, k2-1):
            angulo = jo[i,j]
            if -np.pi / 8 < angulo <= np.pi / 8:
                if jm[i,j] >= jm[i, j-1] and jm[i,j] >= jm[i, j+1]:
                    jn[i,j] = jm[i,j]
            elif np.pi / 8 < angulo <= 3 * np.pi / 8:
                if jm[i,j] >= jm[i-1, j+1] and jm[i,j] >= jm[i+1, j-1]:
                    jn[i,j] = jm[i,j]
            elif -np.pi / 8 >= angulo > -3 * np.pi / 8:
                if jm[i,j] >= jm[i-1, j-1] and jm[i,j] >= jm[i+1, j+1]:
                    jn[i,j] = jm[i,j]
            elif angulo > 3 * np.pi / 8 or angulo <= -3 * np.pi / 8:
                if jm[i,j] >= jm[i-1, j] and jm[i,j] >= jm[i+1, j]:
                    jn[i,j] = jm[i,j]
    return jn / np.max(jn)

U_MAX = 0.15
U_MIN = 0.03
def umbral_por_histeresis(im, jo):
    r = np.zeros(jm.shape, dtype=np.float)
    k1, k2 = jm.shape
    for i in range(1, k1-1):
        for j in range(1, k2-1):
            if im[i, j] >= U_MIN:
                r[i, j] = im[i,j]
            if im[i, j] >= U_MAX:
                angulo = jo[i,j]
                if -np.pi / 8 < angulo <= np.pi / 8:
                    if im[i-1, j] >= U_MIN:
                        r[i-1, j] = U_MAX
                    if im[i+1, j] >= U_MIN:
                        r[i+1, j] = U_MAX
                elif np.pi / 8 < angulo <= 3 * np.pi / 8:
                    if im[i-1, j-1] >= U_MIN:
                        r[i-1, j-1] = U_MAX
                    if im[i+1, j+1] >= U_MIN:
                        r[i+1, j+1] = U_MAX
                elif -np.pi / 8 >= angulo > -3 * np.pi / 8:
                    if im[i-1, j+1] >= U_MIN:
                        r[i-1, j+1] = U_MAX
                    if im[i+1, j-1] >= U_MIN:
                        r[i+1, j-1] = U_MAX
                elif angulo > 3 * np.pi / 8 or angulo <= -3 * np.pi / 8:
                    if im[i, j-1] >= U_MIN:
                        r[i, j-1] = U_MAX
                    if im[i, j+1] >= U_MIN:
                        r[i, j+1] = U_MAX
    idx = r >= U_MAX
    r[idx] = 1.0
    idx = r < U_MAX
    r[idx] = 0.0
    return r


im1 = np.asarray(Image.open(argv[1]).convert('L'))
im2 = gaussiano(im1)
jm, jo = edge_detection(im2, argv[2])
im3 = umbral_por_histeresis(supresion_de_no_maximos(jo, jm), jo)

print(jo)
print(jm)
side_by_side.sbys([im1, im3],
                  ["Original", 'Canny (con '+argv[2]+')'],
                  argv=None if len(argv) <= 3 else argv[3])
