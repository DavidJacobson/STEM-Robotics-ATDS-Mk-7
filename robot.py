### Main File



#Imports
import RPi.GPIO as GPIO
import time
from servo import Servo
from display import Display
from sonic import Sonic

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
		self.turret_servo = Servo(5)
		self.sonic = Sonic(16, 18)

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
	for each in range(100):
		time.sleep(1)
		print reggie.sonic.get_dist()	
except KeyboardInterrupt:
	reggie.stop()
	GPIO.cleanup()
