import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

src = cv2.imread('/home/pi/Desktop/blobby.jpg')
ret, thresh = cv2.threshold(src,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU);
connectivity = 4;
output = cv2.connectedComponentsWithStats(thresh, connectivity , cv2.CV_325);
num_labels = output[0];
labels = outoput[1];
stats = output[2];
centroids = outputs[3];
