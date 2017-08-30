import numpy as np
from PIL import Image
from sys import argv
import side_by_side
import utils

def histogram(im):
	return side_by_side.histogram_hsi(im)


def uniform_hist(im):
    histogram_h, accum_h, histogram_s, accum_s, histogram_i, accum_i  = histogram(im)
    rango_busqueda = [float(i) / len(accum_i) for i in range(len(accum_i))]
    def w_dot(r):
        wi = accum_i[side_by_side.search_not_exact(r[2], rango_busqueda)]
        return [r[0], r[1], wi]
    ret = im.copy()
    for i in range(ret.shape[0]):
        for j in range(ret.shape[1]):
            ret[i][j] = w_dot(ret[i][j])
    return ret

im1 = np.asarray(Image.open(argv[1]).convert('RGB'))
im2 = utils.to_hsi(im1)
im3 = uniform_hist(im2)
im4 = utils.to_rgb(im3)
side_by_side.sbys_histogram([im1, im2, im3, im4], ['rgb', 'hsi', 'hsi', 'rgb']) 
