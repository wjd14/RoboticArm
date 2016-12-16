from ax12 import Ax12;
import RPi.GPIO as GPIO;
import time;
self = Ax12();


#ifsafetomove
self.moveSpeed(3, 203, 50);

self.moveSpeed(2, 494, 50);
time.sleep(2);
self.moveSpeed(4, 664, 50);
time.sleep(2);
self.moveSpeed(1, 512, 50);

time.sleep(6);

#self.moveSpeed(1, 810, 70);
