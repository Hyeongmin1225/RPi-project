
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

RED_led=11
BLUE_led=12
GREEN_led=13
while 1 : 
    GPIO.setup(RED_led,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BLUE_led,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(GREEN_led,GPIO.OUT, initial=GPIO.LOW)
    
    GPIO.output(RED_led, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(RED_led, GPIO.LOW)
    time.sleep(1)
    
    GPIO.output(BLUE_led, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(BLUE_led, GPIO.LOW)
    time.sleep(1)
    
    GPIO.output(GREEN_led, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(GREEN_led, GPIO.LOW)
    time.sleep(1)
    