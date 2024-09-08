#!/usr/bin/env python3
"""
PWM Tone Generator for 'Twinkle Twinkle Little Star'
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

G = 392.00
D = 587.33
E = 659.25
C = 523.25
B = 493.88
A = 440.00

twinkle_melody = [
    G, G, D, D, E, E, D,  # "Twinkle twinkle little star"
    C, C, B, B, A, A, G,  # "How I wonder what you are"
    D, D, C, C, B, B, A,  # "Up above the world so high"
    D, D, C, C, B, B, A,  # "Like a diamond in the sky"
    G, G, D, D, E, E, D,  # "Twinkle twinkle little star"
    C, C, B, B, A, A, G   # "How I wonder what you are"
]

twinkle_durations = [
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0,  
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0,  
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0,  
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0,  
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0,  
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0   
]

def playtone(frequency: float, duration: float) -> None:
    if frequency == 0:
        utime.sleep(duration) 
    else:
        speaker.duty_u16(1000)
        speaker.freq(int(frequency))
        utime.sleep(duration)
    speaker.duty_u16(0) 


def quiet():
    speaker.duty_u16(0)

print("Playing 'Twinkle Twinkle Little Star'")

for i in range(len(twinkle_melody)):
    playtone(twinkle_melody[i], twinkle_durations[i])

# Turn off the PWM
quiet()

