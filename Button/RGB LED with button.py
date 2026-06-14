from machine import Pin
from time import sleep

red= Pin(15, Pin.OUT)
green= Pin(14, Pin.OUT)
blue= Pin(13, Pin.OUT)

button= Pin(16, Pin.IN, Pin.PULL_UP)

CurrentButton= 0
PreviousButton= 1		#if we use 0 to initialize, it may behave unexpectedly
count= 0

def colour(r,g,b):
    red.value(r)
    green.value(g)
    blue.value(b)
    
colour (1,1,1)

while True:
    CurrentButton= button.value()
    print(CurrentButton)
    
    if CurrentButton== 0 and PreviousButton== 1:
        count+= 1
        if count== 1:
            colour(0,1,1)
        elif count== 2:
            colour(1,0,1)
        elif count== 3:
            colour(1,1,0)
        elif count== 4:
            colour(0,0,0)
        else:
            count= 0
            colour(1,1,1)
    
    PreviousButton= CurrentButton
    sleep(.1)
