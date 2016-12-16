import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;
from matplotlib import pyplot as plt

img = cv2.imread('lit2.jpg', 0)
edges = cv2.Canny(img, 140, 150)
i = 0;
kernel = np.ones((30,30), np.uint8)

plt.imshow(edges,cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.savefig('edges.jpg')

img = cv2.imread('edges.jpg', 0)
ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)

cv2.imwrite('binarized.jpg',thresh1)

img = cv2.imread('binarized.jpg')
dilation = cv2.dilate(img, kernel, iterations = 1)
cv2.imwrite('dilatedimg2.jpg', dilation)

im = cv2.imread('dilatedimg2.jpg', cv2.IMREAD_GRAYSCALE)
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 1
params.maxThreshold = 200

#Filter By Color.
params.filterByColor = True;
params.blobColor = 255

# Filter by Area.
params.filterByArea = True;
params.minArea = 10

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1


# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (255,180,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

x = keypoints[i].pt[0]
y = keypoints[i].pt[1]

for i in range (0, len(keypoints)):
        x = keypoints[i].pt[0]
        y = keypoints[i].pt[1]
        print(int(x),int(y))

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

cv2.imwrite('test1objs.jpg', im_with_keypoints)

print(len(keypoints));

#print(img.shape);


