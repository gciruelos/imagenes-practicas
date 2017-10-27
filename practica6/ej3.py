import side_by_side
import convolution
import numpy as np
from PIL import Image
from sys import argv
import math

kirsch_1 = np.zeros((3,3), dtype=np.float);
kirsch_1[0,0:2] = 5
kirsch_1[2,0:2] = -3
kirsch_1[1,0] = -3
kirsch_1[1,2] = -3

def n_kirsch(k):
    kirsch_n = np.zeros((3,3), dtype=np.float);
    kirsch_n[0,0] = k[0,1]
    kirsch_n[0,1] = k[0,2]
    kirsch_n[0,2] = k[1,2]
    kirsch_n[1,2] = k[2,2]
    kirsch_n[2,2] = k[2,1]
    kirsch_n[2,1] = k[2,0]
    kirsch_n[2,0] = k[1,0]
    kirsch_n[1,0] = k[0,0]
    return kirsch_n

kirschs = [
    kirsch_1,
    n_kirsch(kirsch_1),
    n_kirsch(n_kirsch(kirsch_1)),
    n_kirsch(n_kirsch(n_kirsch(kirsch_1))),
    n_kirsch(n_kirsch(n_kirsch(n_kirsch(kirsch_1)))),
    n_kirsch(n_kirsch(n_kirsch(n_kirsch(n_kirsch(kirsch_1))))),
    n_kirsch(n_kirsch(n_kirsch(n_kirsch(n_kirsch(n_kirsch(kirsch_1)))))),
    n_kirsch(n_kirsch(n_kirsch(n_kirsch(n_kirsch(n_kirsch(n_kirsch(kirsch_1)))))))]

def op_kirsch(im):
    r = np.zeros(im.shape, dtype=float)
    for i in range(8):
        r = np.maximum(r, convolution.convolution(im, kirschs[i]))
    return r


im1 = np.asarray(Image.open(argv[1]).convert('L'))
im2 = op_kirsch(im1)
side_by_side.sbys([im1, im2])
