import sys
import math;

class plotter:
    ox = 264; #obj x in px
    oy = 157; #obj y
    
    
    #plot the point in terms of centimeters, relative to our arm lengths.
    #takes the x and y pixel coordinates of the object
    def convert(self, px, py):
        cx = 302; #center x val in px
        cy = 165; #center y val
        cmCoordinates =[];
        ydif = (cy-py)/30.9 #conversion factor to cm
        xdif = (cx-px)/30.9
        xcm = 0-xdif
        ycm = 16.2-ydif;

        dis = math.sqrt(ycm**2 + xcm**2)
        angle = math.degrees(math.atanh(xcm/ycm));
        #print (xcm)
        #print (ycm)
        #print(dis)
        #print(angle)
        #print (xdif)
        #print (ydif)
        cmCoordinates.append(dis)
        cmCoordinates.append(angle);
        return cmCoordinates;

    def clearList():
        cmCoordinates.clear();
        return cmCoordinates;
