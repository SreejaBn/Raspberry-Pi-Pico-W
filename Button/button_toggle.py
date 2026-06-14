from machine import Pin
from time import sleep

myButton= Pin(14, Pin.IN, Pin.PULL_UP)
led= Pin(15, Pin.OUT)
butPS= 0
butCS= 0

while True:
    butCS= myButton.value()
    print(butCS)
    
    if butPS ==0 and butCS== 1:
        led.value(not led.value())
    
    butPS= butCS
    sleep(.2)
