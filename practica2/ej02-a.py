import numpy as np
from PIL import Image
from sys import argv
import side_by_side
import utils

c = float(argv[2])

def escalar(hsi):
    return [hsi[0], max(0, min(255, c * hsi[1])) , hsi[2]]

def transformacion_puntual(im, f):
    ret = im.copy()
    for i in range(ret.shape[0]):
        for j in range(ret.shape[1]):
            ret[i][j] = f(ret[i][j])
    return ret

im1 = np.asarray(Image.open(argv[1]).convert('RGB'))
im2 = utils.to_hsi(im1)
im3 = transformacion_puntual(im2, escalar)
im4 = utils.to_rgb(im3)
side_by_side.sbys_histogram([im1, im2, im3, im4], ['rgb', 'hsi', 'hsi', 'rgb'],
                            argv=argv[3] if len(argv)>3 else None)
