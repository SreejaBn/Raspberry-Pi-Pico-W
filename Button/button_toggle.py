from machine import Pin
from time import sleep

myButton= Pin(14, Pin.IN, Pin.PULL_UP)
led= Pin(15, Pin.OUT)
butPS= 0        #button previous state
butCS= 0        #button current state
ledS= 0         #button state

while True:
    butCS= myButton.value()
    print(butCS)
    
    if butPS ==1 and butCS== 0:
        ledS = not ledS
        led.value(ledS)
    
    butPS= butCS
    sleep(.2)
