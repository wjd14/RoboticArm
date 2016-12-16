from serial import Serial;
self = Ax12();
import math;

objectAngle = 0;
distanceAway = 0;

# move to the correct angle to pick up the object gotten from the array
self.moveSpeed(1, objectAngle, 50)

