import I2C_driver
import RPi.GPIO as GPIO 
import time 

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
    mylcd = I2C_driver.lcd()
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
        if duty_ratio == 0 : 
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            time.sleep(1)
            mylcd.lcd_display_string("0 stage'", 1)
            mylcd.lcd_display_string("0'", 2)
        elif duty_ratio == 1 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            time.sleep(1)
            mylcd.lcd_display_string("1 stage'", 1)
            mylcd.lcd_display_string("15'", 2)
        elif duty_ratio == 2 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            mylcd.lcd_display_string("2 stage'", 1)
            mylcd.lcd_display_string("30'", 2)
            GPIO.output(seg, fnd[duty_ratio])
        elif duty_ratio == 3 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("3 stage'", 1)
            mylcd.lcd_display_string("45'", 2)
        elif duty_ratio == 4 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("4 stage'", 1)
            mylcd.lcd_display_string("60'", 2)
        elif duty_ratio == 5 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("5 stage'", 1)
            mylcd.lcd_display_string("75'", 2)
        elif duty_ratio == 6 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("6 stage'", 1)
            mylcd.lcd_display_string("90'", 2)
        elif duty_ratio == 7 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("7 stage'", 1)
            mylcd.lcd_display_string("105'", 2)
        elif duty_ratio == 8 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("8 stage'", 1)
            mylcd.lcd_display_string("120'", 2)
        elif duty_ratio == 9 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("9 stage'", 1)
            mylcd.lcd_display_string("135'", 2)
        elif duty_ratio == 10 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("10 stage'", 1)
            mylcd.lcd_display_string("150'", 2)
        elif duty_ratio == 11 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("11 stage'", 1)
            mylcd.lcd_display_string("165'", 2)
        elif duty_ratio == 12 :
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            GPIO.output(seg, fnd[duty_ratio])
            mylcd.lcd_display_string("12 stage'", 1)
            mylcd.lcd_display_string("180'", 2)
        else :
            duty_ratio= 0
            Servo.ChangeDutyCycle(duty_ratio)
        if duty_ratio > MaxDuty:
            duty_ratio= 0
            Servo.ChangeDutyCycle(duty_ratio)
            GPIO.output(seg, fnd[0])
        
    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')
    

if __name__ == '__main__':
    main()
    
