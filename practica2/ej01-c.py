import numpy as np
from PIL import Image
from sys import argv
import side_by_side
import utils

im1 = np.asarray(Image.open(argv[1]).convert('RGB'))
im2 = utils.to_hsi(im1)
side_by_side.sbys_histogram([im1, im2], ['rgb', 'hsi'], argv=argv[2] if len(argv)>2 else None)
