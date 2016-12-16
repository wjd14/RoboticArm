from picamera import PiCamera
from time import sleep

camera = PiCamera();

pic_name = 'img'
pic_num = 0;

def prepImage(num):
    pic = pic_name + str(num);
    return pic;


while(pic_num < 11):
    image = prepImage(pic_num) + '.jpg';
    camera.capture(image);
    pic_num+=1;
    
