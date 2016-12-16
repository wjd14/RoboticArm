from picamera import PiCamera
from time import sleep
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
camera = PiCamera();

#camera.capture('test2.jpg');

img = cv2.imread('blobby.jpg',0)

cv2.imshow('window', img);
cv2.waitKey(0);
cv2.destroyAllWindows();
