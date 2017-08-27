
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image
import numpy as np

def sbys(ims, titles=None, argv=None, m=1):
    imgs = list(map(Image.fromarray, ims))
    whs = list(map(lambda x: x.size, imgs))
    n = len(whs)
    gs = gridspec.GridSpec(m, n // m)

    for i in range(n):
        plt.subplot(gs[i]).imshow(imgs[i], cmap='gray', vmin=0, vmax=255)
    if titles is not None:
        for i in range(n):
            plt.subplot(gs[i]).set_title(titles[i])
    if argv is not None:
        plt.savefig(argv, bbox_inches='tight')
    else:
        plt.show()

L = 256

def histogram(img):
    histogram = [0 for i in range(L)]
    nm = 0
    for p in np.nditer(img):
        histogram[p] += 1
        nm += 1

    for i in range(256):
        histogram[i] = float(histogram[i]) / nm

    accum = [0 for i in range(L)]
    for i in range(256):
        for j in range(i):
            accum[i] += histogram[j]
            if accum[i] > 1.0: accum[i] = 1.0
    return histogram, accum

def sbys_histogram(ims, titles=None, argv=None):
    imgs = list(map(Image.fromarray, ims))
    n = len(imgs)
    whs = list(map(lambda x: x.size, imgs))

    histograms = list(map(histogram, ims))
    gs = gridspec.GridSpec(
        3, n, width_ratios=[1 for i in range(n)], height_ratios=[3, 1, 1])

    for i in range(n):
        plt.subplot(gs[i]).imshow(imgs[i], cmap='gray', vmin=0, vmax=255)
    for i in range(n):
        plt.subplot(gs[i+n]).plot(range(L), histograms[i][0])
    for i in range(n):
        plt.subplot(gs[i+2*n]).plot(range(L), histograms[i][1])
    if titles is not None:
        for i in range(n):
            plt.subplot(gs[i]).set_title(titles[i])
    if argv is not None:
        plt.savefig(argv, bbox_inches='tight')
    else:
        plt.show()
