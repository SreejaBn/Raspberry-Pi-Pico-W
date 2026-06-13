from machine import Pin
from time import sleep

myButton= Pin(14, Pin.IN, Pin.PULL_UP)
led= Pin(15, Pin.OUT)
ledPS= 0
ledCS= 0

while True:
    butState= myButton.value()
    print(butState)
    sleep(.75)
    
    if butState==0:
        ledCS= not ledPS
    
    led.value(ledCS)
    ledPS= ledCS
