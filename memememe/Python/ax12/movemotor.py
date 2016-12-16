from ax12 import Ax12;
import RPi.GPIO as GPIO;
import time;


self = Ax12();




while True:
    self.move(1, 100);
    time.sleep(0.5)
    self.move(1, 200)
    time.sleep(0.5)
    self.move(1, 300);
    time.sleep(0.5)
    self.move(1, 400);
    time.sleep(0.5)
    self.move(1, 500);
    time.sleep(0.5)
    self.move(1, 600);
    time.sleep(0.5)
    self.move(1, 700);
    



