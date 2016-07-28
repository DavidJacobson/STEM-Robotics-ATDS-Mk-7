### This is the file for the motor class
import RPi.GPIO as GPIO
import time

class Motor:

	def __init__(self, pin1, pin2, pin3):
		print pin1, pin2, pin3
		self.pin1 = pin1
		self.pin2 = pin2
		self.pin3 = pin3
		
		GPIO.setup(pin1, GPIO.OUT)
		GPIO.setup(pin2, GPIO.OUT)
		GPIO.setup(pin3, GPIO.OUT)
	def turn_on(self, wait_time=10):
		GPIO.output(self.pin1, GPIO.HIGH)
		GPIO.output(self.pin2, GPIO.HIGH)
		GPIO.output(self.pin3, GPIO.LOW)
		time.sleep(wait_time)
	def turn_off(self, wait_time=1):
		GPIO.output(self.pin3, GPIO.LOW)
		time.sleep(wait_time)
