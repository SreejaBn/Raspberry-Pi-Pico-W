from machine import Pin
from time import sleep

myButton= Pin(14, Pin.IN, Pin.PULL_UP)
led= Pin(15, Pin.OUT)

while True:
    butState= myButton.value()
    print(butState)
    sleep(.1)
    
    if butState == 0:
        led.value(1)
    else:
        led.value(0)
    
