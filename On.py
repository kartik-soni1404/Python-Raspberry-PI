import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

print "Engine on!!"
GPIO.output(4,GPIO.LOW)