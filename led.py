import machine
import time
from machine import Pin
LED=Pin(2,Pin.OUT)
#LED2=Pin(33,Pin.OUT)
def LEDconnect() :
    #LED2.value(0)
    LED.value(0)
    time.sleep(0.5)
    LED.value(1)
    time.sleep(0.5)
    
def LEDready() :
    LED.value(1)
    #LED2.value(0)
def LEDfail() :
    LED.value(0)
def LEDflash() :
    LED.value(0)
    time.sleep(0.2)
    LED.value(1)
    time.sleep(0.2)
    
    
