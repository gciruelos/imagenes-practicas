import numpy as np
import math

def convolution(img, kernel):
    K1, K2 = img.shape
    N1, N2 = kernel.shape
    r = np.zeros(img.shape, dtype=np.uint8)
    rf = np.zeros(img.shape, dtype=np.float)
    # r[k1, k2] = \sum_n1 \sum_n2 kernel[n1,n2] img[k1 - n1, k2 -n2]
    #
    # 00 01 02   00 10 20
    # 10 11 12 * 01 11 21
    # 20 21 22   02 12 22
    #
    for k1 in range(K1):
        for k2 in range(K2):
            index = (k1, k2)
            indices = [((n1 + N1 // 2, n2 + N2 // 2),
                        ((k1 - n1) % K1, (k2 - n2) % K2)) for n1 in range(-(N1-1)//2, (N1-1)//2 + 1) for n2 in range(-(N2-1)//2, (N2-1)//2 + 1)]
            resultado = sum(kernel[i[0]] * img[i[1]] for i in indices)
            rf[index[0], index[1]] = resultado
    return rf

def scale(img):
    K1, K2 = img.shape
    r = np.zeros(img.shape, dtype=np.uint8)
    maximum = 0.0
    minimum = 0.0
    for k1 in range(K1):
        for k2 in range(K2):
            if img[k1,k2] > maximum: maximum = img[k1,k2]
            if img[k1,k2] < minimum: minimum = img[k1,k2]
    print(maximum, minimum)
    r = np.vectorize(lambda x: 255 * (x - minimum) / (maximum - minimum))(img)
    return r

def apply_threshold(img, t):
    idx = img[:,:] < t
    img[idx] = t
    img[:,:] *= 255. / (255. - t)
    img[:,:] -= t * 255. / (255. - t)
    return img
