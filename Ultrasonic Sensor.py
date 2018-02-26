from __future__ import print_function
import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO_TRIGGER = 20
GPIO_ECHO    = 21
temperature = 20
speedSound = 33100 + (0.6*temperature)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
GPIO.output(GPIO_TRIGGER, False)
def measure():
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()
  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()
    elapsed = stop-start
  distance = (elapsed * speedSound)/2
  return distance
def back():
	GPIO.output(17,GPIO.LOW)
	GPIO.output(19,GPIO.LOW)
	GPIO.output(26,GPIO.HIGH)
	GPIO.output(27,GPIO.HIGH)
def stop():
	GPIO.output(17,GPIO.LOW)
	GPIO.output(19,GPIO.LOW)
	GPIO.output(26,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
def right():
	GPIO.output(19,GPIO.LOW)
	GPIO.output(26,GPIO.HIGH)
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
def front():
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(19,GPIO.HIGH)
	GPIO.output(26,GPIO.LOW)
def left():
	GPIO.output(19,GPIO.HIGH)
	GPIO.output(26,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.HIGH)
def u():
	right()
	left()


try:
  while True:
    distance = measure()
    
    if distance < 20:
	back()
	time.sleep(0.5)
	stop()
	u()
	time.sleep(1.69)
	stop()
	
    if distance > 30:
	front()

    else:
	front()
	time.sleep(0.5)
	print("far")
	stop()
except KeyboardInterrupt:
  GPIO.cleanup()
