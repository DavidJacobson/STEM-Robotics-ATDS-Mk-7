### Main File



#Imports
import RPi.GPIO as GPIO
import time
from servo import Servo
from display import Display
from sonic import Sonic
from motor import Motor


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
		
		self.seven_seg_one = Display(SDI=11, RCLK=12, SRCLK=13)
		self.seven_seg_two = Display(SDI=33, RCLK=32, SRCLK=35)
		
		self.turret_servo = Servo(5, "Turret Servo")
                self.sonic_sensor_servo = Servo(7, "Sonic Servo")
		
		self.sonic = Sonic(16, 18)
	
		self.servos = [self.sonic_sensor_servo, self.turret_servo]
 
		self.motor = Motor(21, 26, 29)
	def zero_servos(self):
		print "[*]Calibrating"
		self.sonic_sensor_servo.turn(0, 2)
		self.turret_servo.turn(0, 2)
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
		#TODO change this to a gen
		while True:		
			for deg in self.degrees:
				self.turret_servo.turn(deg, 1)
				x = self.sonic.get_dist()
				if x != None:
					
					# TODO Go into fire() from here
					return

			for deg in range(0, 101, 10)[::-1]: # Now we reverse
				x = self.sonic.get_dist()
                                if x != None:

                                        # TODO Go into fire() from here
                                        return


##Main
try:
	with open("welcome", "r") as welcome_file:
		print welcome_file.read()
	reggie = Robot('reggie', 100)
#	reggie.zero_servos()
#	reggie.main()
	for each in range(100): reggie.output_value(each)
#	reggie.motor.turn_on()
	time.sleep(1)
#	reggie.motor.turn_off()
except KeyboardInterrupt:
	GPIO.cleanup()
