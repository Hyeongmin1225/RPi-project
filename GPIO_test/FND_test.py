

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

seg = [8,10,11,12,13,15,16,18]
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

fnd = [(1,1,1,1,1,1,0,0),
    (0,1,1,0,0,0,0,0),
    (1,1,0,1,1,0,1,0),
    (1,1,1,1,0,0,1,0),
    (0,1,1,0,0,1,1,0),
    (1,0,1,1,0,1,1,0),
    (1,0,1,1,1,1,1,0),
    (1,1,1,0,0,0,0,0),
    (1,1,1,1,1,1,1,0),
    (1,1,1,1,0,1,1,0)]


# GPIO.output(seg, fnd[0])

for i in range (10) :
    GPIO.output(seg, fnd[i])
    time.sleep(1)
