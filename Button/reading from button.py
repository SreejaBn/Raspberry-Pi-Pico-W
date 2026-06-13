from machine import Pin
from time import sleep

myButton= Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    butState= myButton.value()
    print(butState)
    sleep(.1)
