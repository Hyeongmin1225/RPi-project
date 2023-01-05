import RPi.GPIO as GPIO 
import time 
import I2C_driver

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
    (1,1,1,1,0,1,1,0)]
    
    
    seg = [31,32,33,35,36,37,38,40]
    #      a,b ,c ,d ,e ,f ,g ,dp
    
    duty_ratio= 2
    MaxDuty= 12
    PWMpin= 12
    PinTrig=16
    PinEcho=18
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PinTrig, GPIO.OUT) 
    GPIO.setup(PinEcho, GPIO.IN) 
    GPIO.setup(PWMpin, GPIO.OUT) 
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
    Servo=GPIO.PWM(PWMpin, 50) 
    Servo.start(0)
    time.sleep(1)
    startTime=0
    stopTime=0
    mylcd = I2C_driver.lcd()
    while True:
        Servo.ChangeDutyCycle(duty_ratio)
        GPIO.output(PinTrig, False) 
        time.sleep(2)
        # trigger
        
        GPIO.output(PinTrig, True) 
        time.sleep(0.00001) 
        GPIO.output(PinTrig, False) 
        # echo
        while GPIO.input(PinEcho) == 0: 
            startTime = time.time()
        while GPIO.input(PinEcho) == 1: 
            stopTime = time.time()
        Time_interval= stopTime - startTime
        Distance = Time_interval * 17000
        Distance = round(Distance, 2)
        Distance1 = str(Distance)
        
        length = "Distance " + Distance1 +"cm"
        mylcd.lcd_display_string("Door close", 1)
        mylcd.lcd_display_string(length, 2)
         
        
        
        if Distance<10 :
            duty_ratio = 10
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            mylcd.lcd_display_string("Door open", 1)
            GPIO.output(seg, fnd[3])
            time.sleep(1)
            GPIO.output(seg, fnd[2])
            time.sleep(1)
            GPIO.output(seg, fnd[1])
            time.sleep(1)
            duty_ratio= 3
            Servo.ChangeDutyCycle(duty_ratio)
            
        else :
            duty_ratio= 3
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            

    Servo.stop()
    GPIO.cleanup()
if __name__ == '__main__':
    main()