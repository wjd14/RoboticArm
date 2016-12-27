import sys;
import math;
import time;
from ax12 import Ax12;

motor = Ax12();
class Mover:
    
    def move(self, number, ticks, speed):
        motor.moveSpeed(number, ticks, speed);
        return;

    def read(self, number):
        return self.read(number);
    def talk(self):
        print('hi');
