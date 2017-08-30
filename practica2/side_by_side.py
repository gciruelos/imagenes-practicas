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
    return histogram_r, accum_r, histogram_g, accum_g, histogram_b, accum_b

SAMPLES = 500
dom_h = [2*np.pi * float(i) / float(SAMPLES) for i in range(SAMPLES)]
dom_s = [float(i) / float(SAMPLES) for i in  range(SAMPLES)]
dom_i = [float(i) / float(SAMPLES) for i in  range(SAMPLES)]

def search_not_exact(needle, haystack):
    lo = 0
    hi = len(haystack)
    while lo + 1 < hi and lo + (hi - lo) // 2 < len(haystack) - 1:
        mid = lo + (hi - lo) // 2 
        if haystack[mid] <= needle < haystack[mid+1]:
            return mid
        elif haystack[mid] > needle:
            hi = mid
        else:
            lo = mid
    return lo


def histogram_hsi(img):
    histogram_h = [0 for i in range(SAMPLES)]
    histogram_s = [0 for i in range(SAMPLES)]
    histogram_i = [0 for i in range(SAMPLES)]
    nm = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            p = img[i, j]
            histogram_h[search_not_exact(p[0], dom_h)] += 1
            histogram_s[search_not_exact(p[1], dom_s)] += 1
            histogram_i[search_not_exact(p[2], dom_i)] += 1
            nm += 1

    for i in range(SAMPLES):
        histogram_h[i] = float(histogram_h[i]) / nm
        histogram_s[i] = float(histogram_s[i]) / nm
        histogram_i[i] = float(histogram_i[i]) / nm

    accum_h = [0 for i in range(SAMPLES)]
    accum_s = [0 for i in range(SAMPLES)]
    accum_i = [0 for i in range(SAMPLES)]
    for i in range(SAMPLES):
        for j in range(i):
            accum_h[i] += histogram_h[j]
            accum_s[i] += histogram_s[j]
            accum_i[i] += histogram_i[j]
            if accum_h[i] > 1.0: accum_h[i] = 1.0
            if accum_s[i] > 1.0: accum_s[i] = 1.0
            if accum_i[i] > 1.0: accum_i[i] = 1.0
    return histogram_h, accum_h, histogram_s, accum_s, histogram_i, accum_i

def sbys_histogram(ims, mode, titles=None, argv=None):
    if argv == '--end':
        gs = gridspec.GridSpec(1, 2)
        plt.subplot(gs[0]).imshow(ims[0])
        plt.subplot(gs[1]).imshow(ims[-1])
        plt.show()
        return
    n = len(ims)
    gs = gridspec.GridSpec(
        2*n, 4, width_ratios=[2, 1, 1, 1], height_ratios=[1 for _ in range(2*n)])

    for i in range(n):
        plt.subplot(gs[2*i:2*i+2, 0]).imshow(ims[i])
    for i in range(n):
        if mode[i] == 'rgb':
            histogram_r, accum_r, histogram_g, accum_g, histogram_b, accum_b = histogram_rgb(ims[i])
            plt.subplot(gs[8*i+1]).plot(range(L), histogram_r, 'r-')
            plt.subplot(gs[8*i+2]).plot(range(L), histogram_g, 'g-')
            plt.subplot(gs[8*i+3]).plot(range(L), histogram_b, 'b-')
            plt.subplot(gs[8*i+4+1]).plot(range(L), accum_r, 'r--')
            plt.subplot(gs[8*i+4+2]).plot(range(L), accum_g, 'g--')
            plt.subplot(gs[8*i+4+3]).plot(range(L), accum_b, 'b--')
        elif mode[i] == 'hsi':
            # histogram_h, accum_h, histogram_s, accum_s, histogram_i, accum_i = histogram_hsi(ims[i])
            # plt.subplot(gs[8*i+1]).plot(dom_h, histogram_h, 'k-')
            # plt.subplot(gs[8*i+2]).plot(dom_s, histogram_s, 'k-')
            # plt.subplot(gs[8*i+3]).plot(dom_i, histogram_i, 'k-')
            # plt.subplot(gs[8*i+4+1]).plot(dom_h, accum_h, 'k--')
            # plt.subplot(gs[8*i+4+2]).plot(dom_s, accum_s, 'k--')
            # plt.subplot(gs[8*i+4+3]).plot(dom_i, accum_i, 'k--')
            plt.subplot(gs[2*i:2*i+2, 1]).imshow(ims[i][:,:,0], cmap='gray', vmin=0.0, vmax=2*np.pi)
            plt.subplot(gs[2*i:2*i+2, 2]).imshow(ims[i][:,:,1], cmap='gray', vmin=0.0, vmax=1.0)
            plt.subplot(gs[2*i:2*i+2, 3]).imshow(ims[i][:,:,2], cmap='gray', vmin=0.0, vmax=1.0)
    if titles is not None:
        for i in range(n):
            plt.subplot(gs[i]).set_title(titles[i])
    if argv is not None:
        plt.savefig(argv, bbox_inches='tight')
    else:
        plt.show()
