from machine import Pin, PWM
from time import sleep

button = Pin(15, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(16))

while True:
    if button.value() == 0:
        buzzer.freq(330)          # E4 note
        buzzer.duty_u16(32768)    # 50% duty cycle
    else:
        buzzer.duty_u16(0)        # Silent

    sleep(0.01)
