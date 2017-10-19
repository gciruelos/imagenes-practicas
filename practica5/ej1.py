#  python practica4-1/ej1.py <img1> <hi|low> <3|5>
import numpy as np
import math
from PIL import Image
from sys import argv
import side_by_side
import convolution


low_pass_3 = np.ones((3,3), dtype=np.float); low_pass_3[:,:] = 1./9;
low_pass_5 = np.ones((5,5), dtype=np.float); low_pass_5[:,:] = 1./25;
hi_pass_3 = np.ones((3,3), dtype=np.float); hi_pass_3[:,:] /= -9.0; hi_pass_3[1,1] = 8./9;
hi_pass_5 = np.ones((5,5), dtype=np.float); hi_pass_5[:,:] /= -25.0; hi_pass_5[2,2] = 24./25;

kernels = {"low": {"3": low_pass_3, "5": low_pass_5},
           "hi": {"3": hi_pass_3, "5": hi_pass_5}}


im1 = np.asarray(Image.open(argv[1]).convert('L'))
im2 = convolution.convolution(im1, kernels[argv[2]][argv[3]])

print(im1)
print(im2)

side_by_side.sbys([im1, im2])
