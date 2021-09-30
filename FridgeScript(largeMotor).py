import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #red button
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #green button

GPIO.setup(13,GPIO.OUT) #output 1
GPIO.setup(15,GPIO.OUT) #output 2
GPIO.setup(16,GPIO.OUT) #output 3
GPIO.setup(18,GPIO.OUT) #output 4
           
GPIO.output(13,False)
GPIO.output(15,False)
GPIO.output(16,False)
GPIO.output(18,False)

speed = 0.07
           
while True:
    
    if (GPIO.input(7) == GPIO.HIGH) & (GPIO.input(8) != GPIO.HIGH): #red button
        GPIO.output(13,True)
        GPIO.output(15,False)
        GPIO.output(16,False)
        GPIO.output(18,False)
        time.sleep(speed)
        GPIO.output(13,False)
        GPIO.output(15,True)
        GPIO.output(16,False)
        GPIO.output(18,False)
        time.sleep(speed)
        GPIO.output(13,False)
        GPIO.output(15,False)
        GPIO.output(16,True)
        GPIO.output(18,False)
        time.sleep(speed)
        GPIO.output(13,False)
        GPIO.output(15,False)
        GPIO.output(16,False)
        GPIO.output(18,True)
        time.sleep(speed)
        GPIO.output(13,False)
        GPIO.output(15,False)
        GPIO.output(16,False)
        GPIO.output(18,False)
        
    if (GPIO.input(8) == GPIO.HIGH) & (GPIO.input(7) != GPIO.HIGH): #green button
        GPIO.output(13,True)
        GPIO.output(15,False)
        GPIO.output(16,False)
        GPIO.output(18,False)
        time.sleep(speed)
        GPIO.output(13,False)
        GPIO.output(15,False)
        GPIO.output(16,False)
        GPIO.output(18,True)
        time.sleep(speed)
        GPIO.output(13,False)
        GPIO.output(15,False)
        GPIO.output(16,True)
        GPIO.output(18,False)
        time.sleep(speed)
        GPIO.output(13,False)
        GPIO.output(15,True)
        GPIO.output(16,False)
        GPIO.output(18,False)
        time.sleep(speed)
        GPIO.output(13,False)
        GPIO.output(15,False)
        GPIO.output(16,False)
        GPIO.output(18,False)

