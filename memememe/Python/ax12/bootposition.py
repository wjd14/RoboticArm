from ax12 import Ax12;
import RPi.GPIO as GPIO;
import time;

self = Ax12();
#ifsafetomove
self.moveSpeed(3, 1023, 50);
time.sleep(2);
self.moveSpeed(2, 725, 50);
time.sleep(2);
self.moveSpeed(4, 1023, 50);
time.sleep(2);
self.moveSpeed(1, 512, 50);
