import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np;
from matplotlib import pyplot as plt
from PIL import Image, ImageChops;
from plotobjects import plotter;
objectPlotter = plotter();
coordsList = [];
kernel = np.ones((17,17), np.uint8);
class objectFinder:
    #trim the border out of the image to the contouring algorithm doesnt select the whole image
    def trim(self, im):
        bg = Image.new(im.mode, im.size, im.getpixel((50,50)))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return im.crop(bbox)


    def edges(self, im):
        img = cv2.imread(im, 0)
        edges = cv2.Canny(img, 100, 110)
        i = 0;
        kernel = np.ones((17,17), np.uint8)

        #find the edges of the objects

        plt.imshow(edges,cmap = 'gray')
        plt.xticks([]), plt.yticks([])
        plt.savefig('edges.jpg')

    #binarize the image
    def binarize(self):
        img = cv2.imread('edges.jpg', 0)
        ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
        cv2.imwrite('binarized.jpg',thresh1)

    #dilate the edges
    def dilate(self):
        img = cv2.imread('binarized.jpg')
        dilation = cv2.dilate(img, kernel, iterations = 1)
        cv2.imwrite('dilatedimg2.jpg', dilation)

    #trim the borders off the image
        im = Image.open('dilatedimg2.jpg')
        im = self.trim(im)
        im.save('trimmed.jpg');

    #find contours and coordinates
    def contours(self):
        img = cv2.imread('trimmed.jpg')

        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(imgray, 127, 255, 0)

        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(img, contours, -1, (0,255,0), 3)

        cv2.imwrite('objects.jpg', img)

    #go through and save the x and y coordinates in a list.

        for c in contours:
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            coordsList.append(cx);
            coordsList.append(cy)

            print cx, cy
       
    def convertToCm(self, array):
        counter = 0;
        while(counter < len(array)):
            print(objectPlotter.convert(array[counter], array[counter+1]));
            counter+=2;
    @staticmethod
    def run(self, img):
    #use self. since the methods are part of the class
        self.edges(img);
        self.binarize();
        self.dilate();
        self.contours();
        self.convertToCm(coordsList);
        return;

#objectPlotter.convert(264, 157);
obj = objectFinder();
obj.run(obj, 'widerlights.jpg');
