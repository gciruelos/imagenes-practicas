import numpy as np
from PIL import Image
from sys import argv
import side_by_side

L = 256

def histogram(im):
	return side_by_side.histogram_rgb(im)


def uniform_hist(im):
    histogram_r, accum_r, histogram_g, accum_g, histogram_b, accum_b  = histogram(im)
    def w_dot(r):
        wr = accum_r[r[0]]
        wg = accum_g[r[1]]
        wb = accum_b[r[2]]
        return list(map(lambda w: int(w * L - 0.5), [wr, wg, wb]))
    ret = im.copy()
    for i in range(ret.shape[0]):
        for j in range(ret.shape[1]):
            print(i,j)
            ret[i][j] = w_dot(ret[i][j])
    return ret

im1 = np.asarray(Image.open(argv[1]).convert('RGB'))
side_by_side.sbys_histogram([im1, uniform_hist(im1)], ['rgb', 'rgb'],argv=argv[2] if len(argv)>2 else None)
