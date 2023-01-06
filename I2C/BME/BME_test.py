from Adafruit_BME280 import *
import I2C_driver
import time
import RPi.GPIO as GPIO

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
    (0,0,0,0,0,0,0,0)]
    
    duty_ratio= 2
    MaxDuty= 12
    PWMpin= 12
    PinTrig=16
    PinEcho=18
    seg = [31,32,33,35,36,37,38,40]
    #      a,b ,c ,d ,e ,f ,g ,dp
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PinTrig, GPIO.OUT) 
    GPIO.setup(PinEcho, GPIO.IN) 
    GPIO.setup(PWMpin, GPIO.OUT) 
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
    Servo=GPIO.PWM(PWMpin, 50) 
    Servo.start(0)
    time.sleep(1)
    mylcd = I2C_driver.lcd()
    
    # sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, 
    # h_mode=BME280_OSAMPLE_8)
    # degrees = sensor.read_temperature()
    # pascals = sensor.read_pressure()
    # hectopascals = pascals / 100
    # humidity = sensor.read_humidity()
    # print ('Temp = {0:0.3f} deg C'.format(degrees))
    # print ('Pressure = {0:0.2f} hPa'.format(hectopascals))
    # print ('Humidity = {0:0.2f} %'.format(humidity))
    while 1 :
        sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, 
        h_mode=BME280_OSAMPLE_8)
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100
        humidity = sensor.read_humidity()
        degrees = round(degrees, 1)
        deg = str(degrees)
        degr1 = "Degrees : " + deg + "C"
        mylcd.lcd_display_string(degr1, 1)
        
        if degrees < 28 :
            mylcd.lcd_display_string("Fan ON", 2)
            for i in range (0,3) :
                print (i)
                duty_ratio = 10
                Servo.ChangeDutyCycle(duty_ratio)
                time.sleep(0.5)
                duty_ratio = 2
                Servo.ChangeDutyCycle(duty_ratio)
                time.sleep(0.5)

                GPIO.output(seg, fnd[8])
                time.sleep(0.5)
                GPIO.output(seg, GPIO.LOW)
                time.sleep(0.5)
        
        else :
            mylcd.lcd_display_string("Fan OFF", 2)
            duty_ratio= 2
            Servo.ChangeDutyCycle(duty_ratio)
            time.sleep(1)
            
    Servo.stop()
    GPIO.cleanup()
if __name__ == '__main__':
    main()