### Main File



#Imports
import RPi.GPIO as GPIO
import time
from servo import Servo
from display import Display


#Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



#Robot Class
class Robot:
	def __init__(self, name):
		self.name = name
		self.sonic_sensor_servo = Servo(7)
		self.seven_seg_one = Display(SDI=11, RCLK=12, SRCLK=13)
		self.seven_seg_two = Display(SDI=33, RCLK=32, SRCLK=35)
	def stop(self):
		self.sonic_sensor_servo.stop()


	def output_value(self, number):
		number = str(number)
		if len(number) == 2:
			self.seven_seg_one.disp_val(int(number[0]))
			self.seven_seg_two.disp_val(int(number[1]))

		elif len(number) == 1:
			self.seven_seg_one.disp_val(0)
                        self.seven_seg_two.disp_val(int(number[0]))
		else:
			print "NOT A 1 OR 2 DIGIT NUMBER"


##Main
try:
	reggie = Robot('reggie')
	#reggie.sonic_sensor_servo.turn()
	for each in range(1, 100):
		reggie.output_value(each)
	
except KeyboardInterrupt:
	reggie.stop()
	GPIO.cleanup()
