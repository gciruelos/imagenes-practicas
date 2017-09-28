

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image
import numpy as np

def sbysfourier(imgs, titles=None, argv=None, m=1):
    whs = list(map(lambda x: x.size, imgs))
    n = len(whs)
    gs = gridspec.GridSpec(m, n // m)

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
