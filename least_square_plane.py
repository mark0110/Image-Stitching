import numpy as np
import matplotlib.pyplot as mplt
from mpl_toolkits.mplot3d import Axes3D

def lsp():
    var = np.array([[3, 4, 6]])
    var = np.transpose(var)
    x = np.random.rand(1, 500) * 9
    y = np.random.rand(1, 500) * 9
    z = np.zeros((1, 500)) + 1
    A = np.concatenate((x, y, z))
    A = np.transpose(A)
    b = np.matmul(A, var)
    b = np.transpose(b)
    X, Y = np.meshgrid(x, y)
    Z = (var[0]*X + var[1]*Y + var[2])
    noise = np.random.normal(0, 1, 500)
    Znoise = np.matmul(noise, np.transpose(noise))
    Z = Z + Znoise
    fig = mplt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z)
    mplt.show()
    gaussianb = b + noise
    p = np.linalg.pinv(A)
    gaussianb = np.transpose(gaussianb)
    d = np.matmul(p, gaussianb)

    difAbs = np.abs(d - var)

    return difAbs, d

