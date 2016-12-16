import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;

img = cv2.imread('binarized.jpg')
kernel = np.ones((20,20), np.uint8)

dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow('dilation', dilation);
cv2.waitKey(0)

cv2.imwrite('dilatedimg2.jpg', dilation);
