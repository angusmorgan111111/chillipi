import RPi.GPIO as GPIO            # import RPi.GPIO module  

def pin_on(pin):
    GPIO.setmode(GPIO.BCM)           
    GPIO.setup(pin, GPIO.OUT)           
    GPIO.output(pin, 1)

def pin_off(pin):
    GPIO.setmode(GPIO.BCM)             
    GPIO.setup(pin, GPIO.OUT)         
    GPIO.output(pin, 0)

