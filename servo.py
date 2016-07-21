import time
import RPi.GPIO as GPIO
from RPIO import PWM

class Servo:
	def __init__(self, pin_number):
		self.pin_number = pin_number
		GPIO.setup(pin_number, GPIO.OUT)
		self.p = PWM.Servo()
		self.p.set_servo(pin_number, 1200)
	def turn(self, times):
		GPIO.setup(self.pin_number, GPIO.OUT)
		for _ in range(times - 1):
			GPIO.output(self.pin_number, GPIO.HIGH)
