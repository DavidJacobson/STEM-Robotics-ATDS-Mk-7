import time
import RPi.GPIO as GPIO

class Servo:
	def __init__(self, pin_number):
		self.pin_number = pin_number	
		GPIO.setup(pin_number, GPIO.OUT)
		self.p = GPIO.PWM(pin_number, 50)
		self.p.start(7.5)
	def turn(self):
		while True:	
			print "maybe now"
			self.p.ChangeDutyCycle(7.5)
			time.sleep(1)
			print "make it stop"
			self.p.ChangeDutyCycle(2.5)
			time.sleep(1)
	def stop(self):
		self.p.stop()
