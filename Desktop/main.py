import sys;
import math;
import time;
from ax12 import Ax12;
from plotobjects import plotter;
from picturetaker import picturetaker;
from objectFinder import objectfinder;
from pickupobjects import pickerUpper;
from move import mover;

m1ticks = 0;

def main():
    scanningPosition();
    for x in range (0, 9):
        
        #take a picture
        pictureTaker.takeImage(x);
        #next, analyze image for objects, and find their real coordinates
        objectfinder.run('/home/pi/Desktop/Pictures/img' + str(x) + '.jpg');
        

        #rotate to the next spot
        self.rotate(x);
        
    return;


def scanningPosition(self):
    Ax12.moveSpeed(3, 203, 50);
    Ax12.moveSpeed(2, 494, 50);
    time.sleep(2);
    Ax12.moveSpeed(4, 664, 50);
    time.sleep(2);
    Ax12.moveSpeed(1, 200, 50);
    time.sleep(2);
    return;

def rotate(self, position):
    degrees = 20 * position + 20;
    m1ticks = (degrees -122.308)/0.28846;
    mvoer.moveSpeed(1, m1ticks, 50);

def pickUp(self, angle):
    ticks = m1ticks + (objectFinder.coordsList[1] -122.308)/0.28846)
    mover.moveSpeed(1, objectFinder.coordsList[1] + position, 50);
