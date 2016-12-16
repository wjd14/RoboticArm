from picamera import PiCamera
from time import sleep
camera = PiCamera();
import os;
class pictureTaker:

    def takeImage(self, spot):
    #this takes an image and names it with whatever number is fed in
        os.chdir('/home/pi/Desktop/Pictures');
        pic_name = 'img' + str(spot) +'.jpg';
        camera.capture(pic_name);
        return;


b = pictureTaker();

#b.takeSubsequentImages(0);


    #below is a little test code
pic_num = 0;
while(pic_num < 11):
    b.takeImage(pic_num);
    sleep(1);
    pic_num+=1;
