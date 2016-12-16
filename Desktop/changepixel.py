import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;
from matplotlib import pyplot as plt

img = cv2.imread('scan3.jpg');


px = img[100, 100];
print(px);

px = [255, 255, 0]
print(px);

print(img.size)
cv2.imwrite('changedpixel.jpg', img);
