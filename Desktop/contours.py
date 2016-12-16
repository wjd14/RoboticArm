import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;

img = cv2.imread('trimmed.jpg')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imwrite('contours.jpg', img)

cnt = contours[-1];

M = cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print cx
print cy
