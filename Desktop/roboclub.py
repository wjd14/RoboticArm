from picamera import PiCamera
from time import sleep
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
camera = PiCamera();

image = cv2.imread('blobby.jpg')

(b,g,r) = image[0,0]

print('Pixel at (0,0) -red: {}, Green: {}, Blue: {}'.format(r,g,b))

image [0,0] = (0,0,255);

corner = image[0:100, 0:100];

cv2.imshow('Corner', corner);

image[0:100, 0:100] = (255,0,0);

cv2.imshow('New', image)

cv2.waitKey(0)
