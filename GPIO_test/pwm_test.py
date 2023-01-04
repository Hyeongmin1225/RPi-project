
import RPi.GPIO as GPIO
import time

LED =12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED,GPIO.OUT)

PWM_LED = GPIO.PWM(LED,50)
PWM_LED.start(0)

try:
    while True : 
        Duty_led=input('Enter Brightness(0 to 100):')
        duty=int(Duty_led)
        print('Duty rate: ',duty)
        PWM_LED.ChangeDutyCycle(duty)

finally:
    PWM_LED.stop()
    print('Cleaning up!')
    GPIO.cleanup()