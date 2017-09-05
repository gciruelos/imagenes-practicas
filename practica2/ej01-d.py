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
        # La intensidad buscada es la de la acumulada.
        wi = accum_i[side_by_side.search_not_exact(r[2], rango_busqueda)]
        # Como los colores estan dentro de un cono puede que la saturacion sea incorrecta
        # si cambio la intensidad, con lo cual corrigo la saturacion
        if wi > 0.5 and r[1] > 2 - 0.5 * wi:
            s = 2 - 0.5 * wi
        if wi < 0.5 and r[1] > 2 * i:
            s = 2 * wi
        else:
            s = r[1]
        return [r[0], s, wi]
    ret = im.copy()
    for i in range(ret.shape[0]):
        for j in range(ret.shape[1]):
            ret[i][j] = w_dot(ret[i][j])
    return ret

im1 = np.asarray(Image.open(argv[1]).convert('RGB'))
im2 = utils.to_hsi(im1)
im3 = uniform_hist(im2)
im4 = utils.to_rgb(im3)
side_by_side.sbys_histogram([im1, im2, im3, im4], ['rgb', 'hsi', 'hsi', 'rgb'],
                                argv=argv[2] if len(argv)>2 else None)
