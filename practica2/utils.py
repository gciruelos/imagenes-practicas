import numpy as np

L = 255
EPS = 0.00000001

def to_hsi(img):
    imgr = img.copy().astype(np.float32)
    for i_ in range(imgr.shape[0]):
        for j_ in range(imgr.shape[1]):
            p = imgr[i_, j_]
            r = float(p[0]) / L
            g = float(p[1]) / L
            b = float(p[2]) / L
            cuenta_h = np.arccos(
                (0.5 * ((r - g) + (r - b))) / (EPS + np.power(np.power(r-g, 2.0) + (r-b)*(g-b), 0.5)))
            if b <= g:
                h = cuenta_h
            else:
                h = 2*np.pi - cuenta_h
            s = 1.0 - 3.0 * float(min(r,g,b)) / (EPS + float(r + g + b))
            i = float(r + g + b) / 3.0
            imgr[i_, j_] = [h, s, i]
    return imgr


def hsi_to_rgb(hsi):
    h = hsi[0]
    s = hsi[1]
    i = hsi[2]
    # arreglo de potenciales problemas (coordenadas fuera del cono).
    if i > 0.5 and s > 2 - 0.5 * i:
        s = 2 - 0.5 * i
    if i < 0.5 and s > 2 * i:
        s = 2 * i

    if h < 2.0 * np.pi / 3.0:
        r = i * (1 + s * np.cos(h)                 / np.cos(np.pi/3.0 - h))
        b = i * (1 - s)
        g = 3 * i - (r + b)
    elif h < 4.0 * np.pi / 3.0:
        g = i * (1 + s * np.cos(h - 2.0*np.pi/3.0) / np.cos(np.pi/3.0 - (h - 2.0*np.pi/3.0)))
        r = i * (1 - s)
        b = 3 * i - (r + g)
    else:
        b = i * (1 + s * np.cos(h - 4.0*np.pi/3.0) / np.cos(np.pi/3.0 - (h - 4.0*np.pi/3.0)))
        g = i * (1 - s)
        r = 3 * i - (g + b)
    if r > 1.0: print(hsi, 'r', r)
    if g > 1.0: print(hsi, 'g', g)
    if b > 1.0: print(hsi, 'b', b)
    r = min(int(256 * r - 0.5), 255)
    g = min(int(256 * g - 0.5), 255)
    b = min(int(256 * b - 0.5), 255)
    return [r, g, b]
    

def to_rgb(img):
    imgr = img.copy().astype(np.uint8)
    for i_ in range(imgr.shape[0]):
        for j_ in range(imgr.shape[1]):
            imgr[i_, j_] = hsi_to_rgb(img[i_, j_])
    return imgr
