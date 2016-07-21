import RPi.GPIO as GPIO
import time
from servo import Servo



GPIO.setmode(GPIO.BOARD)

class Robot:
	def __init__(self, name):
		self.name = name
		self.sonic_sensor_servo = Servo(11)
reggie = Robot('reggie')
reggie.sonic_sensor_servo.turn(50000)
