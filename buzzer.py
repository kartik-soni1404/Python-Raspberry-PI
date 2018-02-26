import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
def beep():
	GPIO.output(14,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(14,GPIO.LOW)
	GPIO.output(15,GPIO.HIGH)
def off():
	GPIO.output(14,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
		
	

try:
  while True:
	  beep()    
except KeyboardInterrupt:
 off()
 GPIO.cleanup()
GPIO.cleanup()

