import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;

from matplotlib import pyplot as plt

a = np.linspace(0,10,100)
b = np.exp(-a)
plt.plot(a,b)
plt.show();

plt.savefig('plot.jpg')
