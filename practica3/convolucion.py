import matplotlib.pyplot as plt

def convolution2d(f, g, minx, maxx):
    def conv2d(f, g, minx, maxx, n1, n2):
        return sum([f(k1, k2) * g(n1-k1, n2-k2) for k1 in range(minx, maxx) for k2 in range(minx, maxx)])
    a = [[conv2d(f, g, minx, maxx, n1, n2) for n1 in range(minx, maxx)] for n2 in list(range(minx, maxx))[::-1]]
    for x in a: print(x)
    plt.imshow(a, cmap='hot', interpolation='nearest', extent=[minx, maxx-1, minx, maxx-1])
    plt.show()
    
    
def f(x, y):
    if (x, y) == (0, 0): return 2
    elif (x, y) == (1, 0): return 5
    elif (x, y) == (2, 0): return 3
    elif (x, y) == (0, 1): return 1
    elif (x, y) == (1, 1): return 4
    elif (x, y) == (2, 1): return 1
    else: return 0

def gi(x, y):
    if (x, y) == (-1, 0): return -1
    elif (x, y) == (0, 0): return 4
    elif (x, y) == (1, 0): return -1
    elif (x, y) == (-1, 1): return 0
    elif (x, y) == (0, 1): return -1
    elif (x, y) == (1, 1): return 1
    elif (x, y) == (-1, -1): return 0
    elif (x, y) == (0, -1): return -1
    elif (x, y) == (1, -1): return 0
    else: return 0

def gii(x, y):
    if (x, y) == (-1, 0): return 1
    elif (x, y) == (0, 0): return 2
    elif (x, y) == (1, 0): return 3
    else: return 0

def giii(x, y):
    if (x, y) == (0, -1): return -1
    elif (x, y) == (0, 0): return 3
    elif (x, y) == (0, 1): return -2
    else: return 0

# convolution2d(f, gi, -1, 7)
convolution2d(f, gii, -1, 4)
# convolution2d(f, giii, -1, 3)
