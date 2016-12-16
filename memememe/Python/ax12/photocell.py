from ax12 import Ax12;
import RPi.GPIO as GPIO;
import time, sys;
self = Ax12();

DEBUG =1;
GPIO.setmode(GPIO.BCM);
def readCell(RCpin):
    reading = 0;
    GPIO.setup(RCpin, GPIO.OUT);
    GPIO.output(RCpin, GPIO.LOW);
    time.sleep(0.1);
    GPIO.setup(RCpin, GPIO.IN);

    while(GPIO.input(RCpin) == GPIO.LOW):
        reading +=1;
   # return reading;

    if reading > 300000:
       return True;
    else:
        return False;
    


while True:
    if readCell(17):
        self.move(1, 600);
        time.sleep(0.5);
        self.move(1, 300);
        time.sleep(0.5);
    else:
        self.setLedStatus(1, True);
        time.sleep(0.5);
        self.setLedStatus(1, False);
        time.sleep(0.5);
  #  print readCell(17);
