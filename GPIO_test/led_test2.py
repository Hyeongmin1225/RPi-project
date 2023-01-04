
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


RED_led=12
BLUE_led=11
GREEN_led=13
while 1 : 
    color = (input('r,g,b 색깔을 입력해주세요:'))
    GPIO.setup(RED_led,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BLUE_led,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(GREEN_led,GPIO.OUT, initial=GPIO.LOW)
    if color == 'r' :
        GPIO.output(RED_led, GPIO.HIGH)
        time.sleep(1)

        # GPIO.output(RED_led, GPIO.LOW)
        # time.sleep(1)
    
    elif color == 'b' :
        GPIO.output(BLUE_led, GPIO.HIGH)
        time.sleep(1)

        # GPIO.output(BLUE_led, GPIO.LOW)
        # time.sleep(1)
    
    elif color == 'g' :
        GPIO.output(GREEN_led, GPIO.HIGH)
        time.sleep(1)

        # GPIO.output(GREEN_led, GPIO.LOW)
        # time.sleep(1)
    
    else :
        GPIO.output(RED_led, GPIO.LOW)
        GPIO.output(BLUE_led, GPIO.LOW)
        GPIO.output(GREEN_led, GPIO.LOW)
        
    