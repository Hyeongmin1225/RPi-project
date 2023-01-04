
import RPi.GPIO as GPIO
import time

LED =12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED, GPIO.OUT)

Duty_led = [90,10,80,20,70,30,60,40,50,100]

PWM_LED = GPIO.PWM(LED,50)
PWM_LED.start(0)

try : 
    for i in range (20) :
        
        duty=int(Duty_led[i])
        print('Duty rate: ',duty)
        PWM_LED.ChangeDutyCycle(duty)
        time.sleep (0.5)

finally:
    PWM_LED.stop()
    GPIO.cleanup()


