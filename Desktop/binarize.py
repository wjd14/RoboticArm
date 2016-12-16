import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;
from matplotlib import pyplot as plt

img = cv2.imread('edges.jpg', 0)

ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)

cv2.imwrite('binarized.jpg',thresh1)
