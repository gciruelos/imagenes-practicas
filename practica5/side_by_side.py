import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image
import numpy as np


def sbys(imgs, titles=None, argv=None, m=1):
    whs = list(map(lambda x: x.size, imgs))
    n = len(imgs)
    gs = gridspec.GridSpec(m, n // m)
    if m == 1:
        plt.figure(figsize=(14, 7))
    elif m == 2:
        plt.figure(figsize=(14, 14))
    elif m == 3:
        plt.figure(figsize=(8, 20))


    for i in range(n):
        plt.subplot(gs[i]).imshow(imgs[i], cmap='gray')
    if titles is not None:
        for i in range(n):
            plt.subplot(gs[i]).set_title(titles[i])
    if argv is not None:
        plt.savefig(argv, bbox_inches='tight')
    else:
        plt.show()
