import machine
import time
import camera
from machine import Pin
import connect
import led
import base64
import json
import urequests as requests
import encode

connect.connect()
SW = Pin(12,Pin.IN)
num = 2
for i in range(5):
    cam = camera.init()
    time.sleep(1)
    print("Camera ready?: ", cam)
    if cam:
        print("Camera ready")
        break
    else :
        camera.deinit()

while num<=10 :
    time.sleep(0.2)
    if (SW.value()==1) :
        num = num+1
    else :
        if(num>0) :
            image = camera.capture()
            with open('/image.jpg', 'wb') as f:
                f.write(image)
            encode.encode()
            num = 0
led.LEDfail()