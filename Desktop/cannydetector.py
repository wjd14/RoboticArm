import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;

from matplotlib import pyplot as plt

img = cv2.imread('scan1.jpg', 0)
edges = cv2.Canny(img, 100, 120)

#plt.subplot(121), plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.imshow(edges,cmap = 'gray')
plt.xticks([]), plt.yticks([])

plt.savefig('foo.jpg');
plt.show()

print(img.shape)
