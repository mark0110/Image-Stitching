import cv2 as cv
import numpy as np

def stitch():
    left = cv.imread("parliament-left.jpg")
    #left = cv.resize(left, (500, 504))
    leftg = cv.cvtColor(left, cv.COLOR_BGR2GRAY)
    right = cv.imread("parliament-right.jpg")
    #right = cv.resize(right, (500, 504))
    rightg = cv.cvtColor(right, cv.COLOR_BGR2GRAY)

    sift = cv.ORB_create()

    left_kp, left_des = sift.detectAndCompute(leftg, None)
    right_kp, right_des = sift.detectAndCompute(rightg, None)

    bfmatch = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    match = bfmatch.match(left_des, right_des)
    match = sorted(match, key = lambda x:x.distance)
    matchpercent = 0.5
    goodmatchnum = int(len(match) * matchpercent)
    match = match[:goodmatchnum]
    points1 = np.zeros((len(match), 2), dtype=np.float32)
    points2 = np.zeros((len(match), 2), dtype=np.float32)

    for i, m in enumerate(match):
        points1[i, :] = left_kp[m.queryIdx].pt
        points2[i, :] = right_kp[m.trainIdx].pt

    points1 = np.float32(points1)
    points2 = np.float32(points2)

    trForm, mask = cv.findHomography(points2, points1, cv.RANSAC, 5.0)
    finImg = cv.warpPerspective(right, trForm, (left.shape[1] + right.shape[1], left.shape[0]))

    finImg[0:left.shape[0], 0:left.shape[1]] = left
    cv.imwrite('output.jpg', finImg)
    finImg = cv.resize(finImg, (int((left.shape[1] + right.shape[1])/4), int(left.shape[0]/4)))

    return finImg