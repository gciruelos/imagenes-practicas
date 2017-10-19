

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image
import numpy as np

def process_mod(img_mod):
    intermedio = np.vectorize(lambda x: np.log(x+1))(img_mod)
    N1, N2 = intermedio.shape
    r = np.zeros(img_mod.shape, dtype=np.float)
    #  1  2         4   3   
    #          ->     
    #  3  4         2   1

    # 1
    for k1 in range(0, N1//2):
        for k2 in range(0, N2//2):
            r[k1 + N1//2][k2 + N2//2] = intermedio[k1][k2]
    # 2
    for k1 in range(0, N1//2):
        for k2 in range(N2//2, N2):
            r[k1 + N1//2][k2 - N2//2] = intermedio[k1][k2]
    # 3
    for k1 in range(N1//2, N1):
        for k2 in range(0, N2//2):
            r[k1 - N1//2][k2 + N2//2] = intermedio[k1][k2]
    # 4
    for k1 in range(N1//2, N1):
        for k2 in range(N2//2, N2):
            r[k1 - N1//2][k2 - N2//2] = intermedio[k1][k2]
    return r


def sbysfourier(imgs, titles=None, argv=None, m=1):
    whs = list(map(lambda x: x.size, imgs))
    n = len(whs)
    gs = gridspec.GridSpec(m, n // m)
    imgs[1] = process_mod(imgs[1])

    plt.figure(figsize=(10,5))
    plt.subplot(gs[0]).imshow(imgs[0], cmap='gray', vmin=0, vmax=255)
    plt.subplot(gs[1]).imshow(imgs[1], cmap='gray')
    plt.subplot(gs[2]).imshow(imgs[2], cmap='gray', vmin=-np.pi, vmax=np.pi)
    if titles is not None:
        for i in range(n):
            plt.subplot(gs[i]).set_title(titles[i])
    if argv is not None:
        plt.savefig(argv, bbox_inches='tight')
    else:
        plt.show()

def sbys3(imgs, titles=None, argv=None, m=1):
    whs = list(map(lambda x: x.size, imgs))
    n = len(whs)
    gs = gridspec.GridSpec(m, n // m)
    plt.subplot(gs[0]).imshow(imgs[0], cmap='gray', vmin=0, vmax=255)
    plt.subplot(gs[1]).imshow(imgs[1], cmap='gray', vmin=0, vmax=255)
    plt.subplot(gs[2]).imshow(imgs[2], cmap='gray', vmin=0, vmax=255)
    if titles is not None:
        for i in range(n):
            plt.subplot(gs[i]).set_title(titles[i])
    if argv is not None:
        plt.savefig(argv, bbox_inches='tight')
    else:
        plt.show()
