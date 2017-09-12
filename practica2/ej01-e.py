import numpy as np
from PIL import Image
from sys import argv
import side_by_side
import utils

def logito(hsi):
    return [hsi[0], hsi[1], np.log(hsi[2] + 1)]

def logitos(hsi):
    return [hsi[0], np.log(hsi[1] + 1), hsi[2]]

def swap(hsi):
    return [hsi[0], hsi[2], hsi[1]]

def transformacion_puntual(im, f):
    ret = im.copy()
    for i in range(ret.shape[0]):
        for j in range(ret.shape[1]):
            ret[i][j] = f(ret[i][j])
    return ret

im1 = np.asarray(Image.open(argv[1]).convert('RGB'))
im2 = utils.to_hsi(im1)
im3 = transformacion_puntual(im2, logito)
im4 = utils.to_rgb(im3)
side_by_side.sbys_histogram([im1, im2, im3, im4], ['rgb', 'hsi', 'hsi', 'rgb'], 
                                argv=argv[2] if len(argv)>2 else None)
