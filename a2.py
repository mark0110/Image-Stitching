import cv2 as cv
import numpy as np

img = cv.imread("city.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
city_ft = np.fft.fft2(city_img)