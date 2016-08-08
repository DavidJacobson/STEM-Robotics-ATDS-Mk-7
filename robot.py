## Main File



#Imports
import RPi.GPIO as GPIO
import time
from servo import Servo
from display import Display
from sonic import Sonic
from motor import Motor
import serial

#Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



#Robot Class
class Robot:
	def __init__(self, name, ammo):
		self.name = name
		self.current_degree = 0
		self.ammunition_count = ammo
		self.degrees = range(0, 101, 10)
		self.serial_connection =  serial.Serial("/dev/ttyACM0", 9600)


	
		self.seven_seg_one = Display(SDI=11, RCLK=12, SRCLK=13)
		self.seven_seg_two = Display(SDI=33, RCLK=32, SRCLK=35)
		
		self.x_axis = Servo(0, "X Axis", self)
		self.y_axis = Servo(1, "Y Axis", self)		
		self.release= Servo(2, "Release", self)
		
		self.sonic = Sonic(16, 18)
	
		self.servos = [self.x_axis, self.y_axis]
 
		self.motor = Motor(37, 38, 40)

	def demo(self):
		self.x_axis.turn(180)
		self.y_axis.turn(170)
		self.x_axis.turn(100)
		self.y_axis.turn(20)
	def calibrate(self):
		print "[*]Calibrating"
		self.x_axis.turn(180, 0.05)
		self.y_axis.turn(90, 0.05)
		#self.release.turn(180, 0.05)
		print "[*]Done"
	def output_value(self, number):
		number = str(number)
		if len(number) == 2:
			self.seven_seg_one.disp_val(int(number[0]))
			self.seven_seg_two.disp_val(int(number[1]))

		elif len(number) == 1:
			self.seven_seg_one.disp_val(0)
                        self.seven_seg_two.disp_val(int(number[0]))
		else:
			print "[-] Attempted to print non-two-digit number: {}".format(number)

	def main(self):
		"""This is to be the main method. It will do the following:
		(1) Rotate the main servo in 10 degree segments
		(2) Stops and scans for an object
		(3) If an object exists, goes into "Firing Mode"
		(4) If not, continues on
		(5) Once it hits 180, it should reverse down to 0
		"""
		while True:
			for deg in range(0, 181, 10):
				self.x_axis.turn(deg, 0.005)
				ob_pres = self.sonic.get_dist()
				if not (ob_pres is None):
					self.y_axis.turn(30)
					print "[!]Preparing to Fire"
					self.motor.fire()
					self.y_axis.turn(90)
			for deg in range(0,181, 10)[::-1]:
				self.x_axis.turn(deg, 0.005)
				ob_pres = self.sonic.get_dist()
				if not (ob_pres is None):
					self.y_axis.turn(30)
					print "[!]Preparing to Fire"
					self.motor.fire()
					self.y_axis.turn(90)
##Main
try:
	with open("welcome", "r") as welcome_file:
		print welcome_file.read()
	reggie = Robot('reggie', 100)
	reggie.calibrate()
	reggie.main()
	GPIO.cleanup()
except KeyboardInterrupt:
	GPIO.cleanup()
	print "[*]Cleanup Successful"
