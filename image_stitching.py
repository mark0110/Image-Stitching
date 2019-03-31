import cv2 as cv
import numpy as np
#import vlfeat as vl
from matplotlib import pyplot as plot


left = cv.imread("parliament-left.jpg")
leftg = cv.cvtColor(left, cv.COLOR_BGR2GRAY)
right = cv.imread("parliament-right.jpg")
rightg = cv.cvtColor(right, cv.COLOR_BGR2GRAY)

sift = cv.ORB_create()

left_kp, left_des = sift.detectAndCompute(leftg, None)
right_kp, right_des = sift.detectAndCompute(rightg, None)

bfmatch = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
match = bfmatch.match(left_des, right_des)
match = sorted(match, key = lambda x:x.distance)
matchpercent = 0.15
goodmatchnum = int(len(match) * matchpercent)
match = match[:goodmatchnum]
points1 = np.zeros((len(match), 2), dtype=np.float32)
points2 = np.zeros((len(match), 2), dtype=np.float32)

for i, m in enumerate(match):
    points1[i, :] = left_kp[m.queryIdx].pt
    points2[i, :] = right_kp[m.trainIdx].pt

points1 = points1.astype(np.float32)
points2 = points2.astype(np.float32)
affmat = cv.getAffineTransform(points1, points2)
warp_right = cv.warpAffine(right, affmat, (right.shape[1], right.shape[0]))

cv.imshow("Window", warp_right)
cv.waitKey(0)
cv.destroyAllWindows()