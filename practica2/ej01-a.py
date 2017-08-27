
import numpy as np
from PIL import Image
from sys import argv
import side_by_side


im1 = np.asarray(Image.open(argv[1]).convert('RGB'))
side_by_side.sbys_histogram([im1], ['rgb']) 
print(im1)

