import RPi.GPIO as GPIO
import time
from servo import Servo


GPIO.setmode(GPIO.BOARD)

#class Servo


class Robot:
	def __init__(self, name):
		self.name = name
		self.sonic_sensor_servo = Servo(7)
	def stop(self):
		self.sonic_sensor_servo.stop()

try:
	reggie = Robot('reggie')
	reggie.sonic_sensor_servo.turn()
except KeyboardInterrupt:
	reggie.stop()
	GPIO.cleanup()
