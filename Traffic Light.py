from machine import Pin
from time import sleep

red= Pin(16, Pin.OUT)
green= Pin(17, Pin.OUT)
blue= Pin(18, Pin.OUT)

def colour(r,g,b):
    red.value(r)
    green.value(g)
    blue.value(b)

while True:
    colour(0,1,1)
    sleep(1)
    colour(0,0,1)
    sleep(1)
    colour(1,0,1)
    sleep(1)
