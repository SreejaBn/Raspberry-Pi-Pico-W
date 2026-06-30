from machine import PWM, Pin 
from time import sleep, sleep_ms

buzzer = PWM(Pin(16))

def play_note(freq, duration):
    if freq == 0:          # Rest (silence)
        buzzer.duty_u16(0)
    else:
        buzzer.freq(freq)
        buzzer.duty_u16(32768)   # 50% duty cycle

    sleep_ms(duration)
    buzzer.duty_u16(0)
    sleep_ms(50)      # Small gap between notes


# Frequencies (Hz)
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

while True:
    play_note(C4, 400)
    play_note(D4, 400)
    play_note(E4, 400)
    play_note(F4, 400)
    play_note(G4, 400)
    play_note(A4, 400)
    play_note(B4, 400)
    play_note(C5, 800)

    sleep(1)
