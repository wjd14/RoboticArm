import sys;
sys.path.append('/usr/local/lib/python2.7/site-packages')
sys.path.append('/home/pi/memememe/Python/ax12')
import math;
import time;
'''
from ax12 import Ax12;
from plotobjects import plotter;
from picturetaker import picturetaker;
from objectFinder import objectfinder;
from pickupobjects import pickerUpper;
'''
from move import Mover;
movey = Mover()
m1ticks = 0;

def main():
    print('hi');
    scanningPosition();
    '''
    for x in range (0, 9):
        self.rotateWithX(x);
        i = 0;
        #take a picture
        pictureTaker.takeImage(x);
        #next, analyze image for objects, and find their real coordinates
        objectfinder.run('/home/pi/Desktop/Pictures/img' + str(x) + '.jpg');
        
        while i < objectFinder.len(coordsList):
            #ticks to go to is current + the angle in coordslist that gets converted to ticks
            #have to figure out if the below code works
            ticks = mover.read(1) + (objectFinder.coordsList[i + 1]-122.308)/.28846;
            #need to rotate to be in line
            mover.move(1,ticks, 50);
            
            
            pickerUpper.calculateTarget(60, objectFinder.coordsList[x]);
            mover.move(2, pickerUpper.angleArray[0], 50);
            mover.move(3, pickerUpper.angleArray[1], 50);
            mover.move(4, pickerUpper.angleArray[2], 50);
            #get back to where you started
            self.rotateWithX(x);
            i +=2;
        #rotate to the next spot
        
        
    return;

'''
def scanningPosition():
    movey.move(3, 203, 50);
    movey.move(2, 494, 50);
    time.sleep(2);
    movey.move(4, 664, 50);
    time.sleep(2);
    movey.move(1, 200, 50);
    time.sleep(2);
    print('Hi');
    return;
'''
def rotateWithX(self, positionX):
    degrees = 20 * positionX + 180;
    m1ticks = (degrees -122.308)/0.28846;
    mover.moveSpeed(1, m1ticks, 50);
    
def pickUp(self, angle):
    ticks = m1ticks + (objectFinder.coordsList[1] -122.308)/0.28846;
    mover.moveSpeed(1, objectFinder.coordsList[1] + position, 50);
'''



def test():
    
#def move(self



#test();

main();
