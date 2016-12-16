import sys;
import math;
import time;
from ax12 import Ax12;
from plotobjects import plotter;
from picturetaker import picturetaker;

def main():
    scanningPosition();
    for x in range (0, 9):
        pictureTaker.takeImage(x);
        #os.chdir('/home/pi/Desktop/Pictures');
        plotter.run('/home/pi/Desktop/Pictures/img' + str(x) + '.jpg');
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
    Ax12.moveSpeed(1, m1ticks, 50);
