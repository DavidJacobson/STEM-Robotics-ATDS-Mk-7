### This is the file for the motor class
import RPi.GPIO as GPIO
import time

class Motor:

	def __init__(self, pin1, pin2, pin3):
		#print pin1, pin2, pin3
		self.pin1 = pin1
		self.pin2 = pin2
		self.enable = pin3
		
		GPIO.setup(pin1, GPIO.OUT)
		GPIO.setup(pin2, GPIO.OUT)
		GPIO.setup(pin3, GPIO.OUT)
		GPIO.output(self.enable, GPIO.LOW)
	def fire(self, wait_time=10):
		GPIO.output(self.enable, GPIO.HIGH) # motor driver enable
		GPIO.output(self.pin1, GPIO.LOW)  # clockwise
		GPIO.output(self.pin2, GPIO.HIGH)
		time.sleep(1.6)
		GPIO.output(self.enable, GPIO.LOW)
		return 

