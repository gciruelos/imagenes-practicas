import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from PIL import Image

L = 256

def histogram_rgb(img):
    histogram_r = [0 for i in range(L)]
    histogram_g = [0 for i in range(L)]
    histogram_b = [0 for i in range(L)]
    nm = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            p = img[i, j]
            histogram_r[p[0]] += 1
            histogram_g[p[1]] += 1
            histogram_b[p[2]] += 1
            nm += 1

    for i in range(L):
        histogram_r[i] = float(histogram_r[i]) / nm
        histogram_g[i] = float(histogram_g[i]) / nm
        histogram_b[i] = float(histogram_b[i]) / nm

    accum_r = [0 for i in range(L)]
    accum_g = [0 for i in range(L)]
    accum_b = [0 for i in range(L)]
    for i in range(256):
        for j in range(i):
            accum_r[i] += histogram_r[j]
            accum_g[i] += histogram_g[j]
            accum_b[i] += histogram_b[j]
            if accum_r[i] > 1.0: accum_r[i] = 1.0
            if accum_g[i] > 1.0: accum_g[i] = 1.0
            if accum_b[i] > 1.0: accum_b[i] = 1.0
    return list(range(L)), histogram_r, accum_r, histogram_g, accum_g, histogram_b, accum_b

def sbys_histogram(ims, mode, titles=None, argv=None):
    imgs = list(map(Image.fromarray, ims))
    n = len(imgs)
    whs = list(map(lambda x: x.size, imgs))

    gs = gridspec.GridSpec(
        2*n, 4, width_ratios=[2, 1, 1, 1], height_ratios=[1 for _ in range(2*n)])

    for i in range(n):
        plt.subplot(gs[i:i+2, 0]).imshow(imgs[i])
    for i in range(n):
        dom, histogram_r, accum_r, histogram_g, accum_g, histogram_b, accum_b = histogram_rgb(ims[i])
        plt.subplot(gs[2*i+1]).plot(range(L), histogram_r, 'r-')
        plt.subplot(gs[2*i+2]).plot(range(L), histogram_g, 'g-')
        plt.subplot(gs[2*i+3]).plot(range(L), histogram_b, 'b-')
        plt.subplot(gs[2*i+4+1]).plot(range(L), accum_r, 'r--')
        plt.subplot(gs[2*i+4+2]).plot(range(L), accum_g, 'g--')
        plt.subplot(gs[2*i+4+3]).plot(range(L), accum_b, 'b--')
    if titles is not None:
        for i in range(n):
            plt.subplot(gs[i]).set_title(titles[i])
    if argv is not None:
        plt.savefig(argv, bbox_inches='tight')
    else:
        plt.show()
