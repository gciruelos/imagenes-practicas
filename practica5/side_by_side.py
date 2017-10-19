import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image
import numpy as np


def sbys(imgs, titles=None, argv=None, m=1):
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
