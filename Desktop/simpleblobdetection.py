import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;
i = 0
# Read image
im = cv2.imread("lit1.jpg", cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()


# Change thresholds
params.minThreshold = 1
params.maxThreshold = 200

#Filter By Color.
params.filterByColor = True;
params.blobColor = 255

# Filter by Area.
params.filterByArea = True#use
params.minArea =500

# Filter by Circularity
params.filterByCircularity = False
params.maxCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False#use
params.minConvexity = 0.3
    
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.1

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
print(im.shape)
