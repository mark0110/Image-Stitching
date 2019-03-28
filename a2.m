close all;
clear;

img = imread('parliament-left.jpg');
grayImg1 = rgb2gray(img);
finImg1 = im2single(grayImg1);

img = imread('parliament-right.jpg');
grayImg2 = rgb2gray(img);
finImg2 = im2single(grayImg2);

%run('vlfeat-0.9.21/toolbox/vl_setup');
[f1, d1] = vl_sift(finImg1);
[f2, d2] = vl_sift(finImg2);

[matches, scores] = vl_ubcmatch(d1, d2);
