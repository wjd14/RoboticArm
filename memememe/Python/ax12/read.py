from ax12 import Ax12;
import RPi.GPIO as GPIO;

import time;

self = Ax12();

trytoSend = True;
resendCounter = 0;
value = 0;

while(trytoSend):
    trytoSend = False;
    try:
        value = self.readPosition(1);
    except:
        trytoSend = True;
        print'Retry';
        resendCounter+=1;
        if(resendCounter>30):
            break;
    print value;
