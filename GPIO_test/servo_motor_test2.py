import RPi.GPIO as GPIO 
import time 
fnd = [(1,1,1,1,1,1,0,0),
    (0,1,1,0,0,0,0,0),
    (1,1,0,1,1,0,1,0),
    (1,1,1,1,0,0,1,0),
    (0,1,1,0,0,1,1,0),
    (1,0,1,1,0,1,1,0),
    (1,0,1,1,1,1,1,0),
    (1,1,1,0,0,0,0,0),
    (1,1,1,1,1,1,1,0),
    (1,1,1,1,0,1,1,0),
    (1,1,1,0,1,1,1,0),
    (0,0,1,1,1,1,1,0),
    (1,0,0,1,1,1,0,0)
    ]
def main():
    duty_ratio= 0
    MaxDuty= 12
    PWMpin= 12
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PWMpin, GPIO.OUT) 
    GPIO.setwarnings(False)
    Servo=GPIO.PWM(PWMpin, 50) 
    Servo.start(0)
    print('Wating for 1 sec') 
    time.sleep(1)
    seg = [31,32,33,35,36,37,38,40]
#      a,b ,c ,d ,e ,f ,g ,dp
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
#      a,b,c,d,e,f,g,dp

    

    
    
    print('Rotating at interval of 0-12 degrees')
    while duty_ratio <= MaxDuty:
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(1)
        GPIO.output(seg, fnd[duty_ratio])
        duty_ratio+= 1
    if duty_ratio > MaxDuty:
        duty_ratio= 0
        Servo.ChangeDutyCycle(duty_ratio)
    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')
if __name__ == '__main__':
    main()
    
