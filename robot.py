### Main File



#Imports
import RPi.GPIO as GPIO
import time
from servo import Servo
from display import Display
#from sonic import Sonic
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
		
		self.x_axis = Servo(0, "X Axis", self.serial_connection)
		self.y_axis = Servo(1, "Y Axis", self.serial_connection)		

		
		#self.sonic = Sonic(16, 18)
	
		self.servos = [self.x_axis, self.y_axis]
 
		self.motor = Motor(37, 38, 40)
	def calibrate(self):
		print "[*]Calibrating"
		self.x_axis.turn(0, 2)
		self.y_axis.turn(0, 2)
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
		(1) Rotate the main servo in 20 degree segments
		(2) Stops and scans for an object
		(3) If an object exists, goes into "Firing Mode" -- TODO
		(4) If not, continues on
		(5) Once it hits 180, it should reverse down to 0
		"""
		for deg in range(0, 101, 10): self.x_axis.turn(deg)


##Main
try:
	with open("welcome", "r") as welcome_file:
		print welcome_file.read()
	reggie = Robot('reggie', 100)
	reggie.calibrate()
	while True:
		reggie.main()
	GPIO.cleanup()
except KeyboardInterrupt:
	GPIO.cleanup()
	print "[*]Cleanup Successful"
