import RPi.GPIO as GPIO 
import time 
# fnd = [(1,1,1,1,1,1,0,0),
#     (0,1,1,0,0,0,0,0),
#     (1,1,0,1,1,0,1,0),
#     (1,1,1,1,0,0,1,0),
#     (0,1,1,0,0,1,1,0),
#     (1,0,1,1,0,1,1,0),
#     (1,0,1,1,1,1,1,0),
#     (1,1,1,0,0,0,0,0),
#     (1,1,1,1,1,1,1,0),
#     (1,1,1,1,0,1,1,0),
#     (1,1,1,0,1,1,1,0),
#     (0,0,1,1,1,1,1,0),
#     (1,0,0,1,1,1,0,0)
#     ]
def main():
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
    duty_ratio= 0
    MaxDuty= 12
    PWMpin= 12
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setwarnings(False)
    GPIO.setup(PWMpin, GPIO.OUT) 
    Servo=GPIO.PWM(PWMpin, 50) 
    Servo.start(0)
    time.sleep(1)
    seg = [31,32,33,35,36,37,38,40]
#      a,b ,c ,d ,e ,f ,g ,dp
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
#      a,b,c,d,e,f,g,dp
# 1=15',2=30' ... 12=180'

    while 1:
        duty_ratio = int(input('0~12을 입력하시오'))
        Servo.ChangeDutyCycle(duty_ratio)
        time.sleep(1)
        GPIO.output(seg, fnd[duty_ratio])
    
        if duty_ratio > MaxDuty:
            duty_ratio= 0
            Servo.ChangeDutyCycle(duty_ratio)
            GPIO.output(seg, fnd[0])
        
    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')
    
    
    
#     while duty_ratio <= MaxDuty:
#         duty_ratio= int(input('0~10입력해주세요'))
#         if duty_ratio>11 :
#             Servo.ChangeDutyCycle(duty_ratio)
#             time.sleep(1)
#             GPIO.output(seg, fnd[duty_ratio])
            
#         else :
#             duty_ratio= 0
#             Servo.ChangeDutyCycle(duty_ratio)
            
#         # if duty_ratio == 0 : 
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         #     time.sleep(1)
#         #     Servo.stop()
#         #     GPIO.cleanup()
#         # elif duty_ratio == 1 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         #     time.sleep(1)
#         #     Servo.stop()
#         #     GPIO.cleanup()
#         # elif duty_ratio == 2 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # elif duty_ratio == 3 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # elif duty_ratio == 4 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # elif duty_ratio == 5 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # elif duty_ratio == 6 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # elif duty_ratio == 7 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # elif duty_ratio == 8 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # elif duty_ratio == 9 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # elif duty_ratio == 10 :
#         #     Servo.ChangeDutyCycle(duty_ratio)
#         #     time.sleep(1)
#         #     GPIO.output(seg, fnd[duty_ratio])
#         # else :
#         #     duty_ratio= 0
#         #     Servo.ChangeDutyCycle(duty_ratio)
#     if duty_ratio > MaxDuty:
#         duty_ratio= 0
#         Servo.ChangeDutyCycle(duty_ratio)
#     Servo.stop()
#     GPIO.cleanup()
#     print('Everythings cleanup')
if __name__ == '__main__':
    main()
    
