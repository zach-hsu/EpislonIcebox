import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #red button
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #green button

GPIO.setup(16,GPIO.OUT) #output 3
GPIO.setup(18,GPIO.OUT) #output 4

GPIO.output(16,False) #initialize output to be 0 on start
GPIO.output(18,False)

speed = 0.07
           
while True:
    
    if (GPIO.input(7) == GPIO.HIGH) & (GPIO.input(8) != GPIO.HIGH): #red button
        GPIO.output(18,True)
        GPIO.output(16,False)

    if (GPIO.input(8) == GPIO.HIGH) & (GPIO.input(7) != GPIO.HIGH): #green button
        GPIO.output(16,True)
        GPIO.output(18,False)
        
    if (GPIO.input(7) != GPIO.HIGH):
        GPIO.output(18,False)
        
    if (GPIO.input(8) != GPIO.HIGH):
        GPIO.output(16,False)
