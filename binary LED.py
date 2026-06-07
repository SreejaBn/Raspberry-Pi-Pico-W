from machine import Pin
from time import sleep

led1= Pin(19, Pin.OUT)
led2= Pin(18, Pin.OUT)
led3= Pin(17, Pin.OUT)
led4= Pin(16, Pin.OUT)

leds = [led1, led2, led3, led4]

while True:
    for count in range(16):
        for bit in range(4):
            leds[bit].value((count >> bit) & 1)

        print(count)
        sleep(1)
