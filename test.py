import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)



GPIO.output(7,GPIO.LOW)
