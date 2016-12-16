from ax12 import Ax12;
import RPi.GPIO as GPIO;
import time;
from serial import Serial;
self = Ax12();
import math;
angleArray = [];
seg1 = 121.5
seg2 = 148
seg3 = 137.5

#angle = 270;
#ticks = 0;

#pie = 512;

#def angleToTicks():
 #   ticks = (angle-122.308)/0.28846
#    print(ticks)
 #   return;

#def ticksToAngle():
#    angle = pie*.28846 + 122.308
#    print(angle)
#    return;

#angleToTicks();
#ticksToAngle();


#m2ticks = 577;#494
#m3ticks = 330;#203
#m4ticks = 854;#821
#calculate the angles on each joint of the arm
#m2degs = -.2955 * m2ticks + 236;
#m3degs = .276 * m3ticks - 146;
#m4degs = -.292 * m4ticks + 149;

#print(m2degs)
#print(m3degs)
#print(m4degs)

def a1degsToTicks(degs):
    ticks = (degs-236)/-.2955;
    print('Angle 1 ticks: %d' %ticks);
    return int(ticks);

def a2degsToTicks(degs):
    ticks = (degs + 146)/.276;
    print('Angle 2 ticks: %d' %ticks);
    return int(ticks);

def a3degsToTicks(degs):
    ticks = (degs-149)/-.292;
    print('Angle 3 ticks: %d' %ticks)
    return int(ticks);


#this part calculates where to move the arm given target height, distance, segment lengths, and net angle(-90)
def calculateTarget(goallowh, goald):
    del angleArray[:]; 
    targetLowEndh = goallowh#60
    targetd = goald;#162
    endpointhSeg3 = targetLowEndh + seg3
    baseh = 61;
    based = 0;
    actualLength = math.sqrt(math.pow((endpointhSeg3-baseh), 2) + math.pow(targetd, 2));#pythagorean theorem to calculate actual distance from origin to target

    #now have an sss triangle, use law of cosines to solve for angles.
    #adding that angle at the start to account for the degrees the resultant is above the ground.

    resultantdegs = math.degrees(math.atan(((seg3 + 61 - targetLowEndh)/targetd)));
    angle1 = resultantdegs + math.degrees(math.acos((math.pow(seg2, 2) - math.pow(actualLength, 2) - math.pow(seg1, 2))/(-2*actualLength*seg1)));

    #180 - angle cuz the servo is oriented backwards. same reason for multiplying by -1.

    angle2 = -1 *(180 -math.degrees(math.acos((math.pow(actualLength, 2)-math.pow(seg2, 2) - math.pow(seg1, 2))/(-2*seg2*seg1))));

    #want the net angle to be -90 (leg 4 vertical), the code below calculates that.

    angle3 = -90 -(angle1+angle2);
    height = seg1 * math.sin(math.radians(angle1)) +seg2 * math.sin(math.radians(angle1 + angle2)) + seg3 *math.sin(math.radians(angle1 + angle2 + angle3)) + 61
    distanceAway =  seg1 * math.cos(math.radians(angle1)) +seg2 * math.cos(math.radians(angle1 + angle2)) + seg3 *math.cos(math.radians(angle1 + angle2 + angle3))
    print(height);
    print(distanceAway)
    print('Angle 1 degrees: %d' %angle1);
    print('Angle 2 degrees: %d' %angle2);
    print('Angle 3 degrees: %d' %angle3);
    angleArray.append(a1degsToTicks(angle1));
    angleArray.append(a2degsToTicks(angle2));
    angleArray.append(a3degsToTicks(angle3));
    print(angleArray[0:3]);
    return;




calculateTarget(61, 146);
