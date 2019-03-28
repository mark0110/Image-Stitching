import scipy as sp
import cv2 as cv
import numpy as np
import scipy.signal as signal

a, b, c = 3, 4, 6
var = np.array([[3, 4, 6]])
var = np.transpose(var)
x = np.random.rand(1, 500) * 9
y = np.random.rand(1, 500) * 9
z = np.zeros((1, 500)) + 1
A = np.concatenate((x, y, z))
A = np.transpose(A)
b = np.matmul(A, var)
b = np.transpose(b)

noise = np.random.normal(0, 1, 500)


gaussianb = b + noise
p = np.linalg.pinv(A)
gaussianb = np.transpose(gaussianb)
d = np.matmul(p, gaussianb)

difAbs = np.abs(d - var)
print(difAbs)
