from machine import Pin
from time import sleep

button= Pin(15, Pin.IN, Pin.PULL_UP)

led1= Pin(16, Pin.OUT)
led2= Pin(17, Pin.OUT)
led3= Pin(18, Pin.OUT)
led4= Pin(19, Pin.OUT)

leds=[led1, led2, led3, led4]

previous= 1
count= 0

while True:
    current= button.value()
    
    if previous== 1 and current== 0:
        count+= 1
        
        if count >15:
            count= 0
            
        for j in range(4):
            leds[j].value((count >>j)&1)
        print(count)
    
    previous= current
    sleep(.1)
