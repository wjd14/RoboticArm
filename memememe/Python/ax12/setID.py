from ax12 import Ax12;
import RPi.GPIO as GPIO;
import time;
from serial import Serial;
self = Ax12();





self.moveSpeed(4, 200, 30);

print (self.readPosition(4));

#little change to test git
