
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

seg = [31,32,33,35,36,37,38,40]
#      a,b ,c ,d ,e ,f ,g ,dp
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
#      a,b,c,d,e,f,g,dp

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

