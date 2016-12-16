import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD);

GPIO.setup(2, GPIO.OUT);

GPIO.output(2, GPIO.HIGH);

time.sleep(10);

GPIO.output(GPIO.LOW);

