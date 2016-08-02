import time
import RPi.GPIO as GPIO

class Servo:
	def __init__(self, pin_number, name, serial):
		self.name = name
		self.serial = serial
		self.pin_number = pin_number
		print "[!]Servo \"{}\" created on pin: {}".format(self.name, self.pin_number)
        
	def turn(self, ang=180, wait_time=1):
#		print "[*] Turning {} deg on servo {}, PIN:  {}, DC: {}".format(ang, self.name, self.pin_number)
		self.serial.write("{},{}\n".format(self.pin_number,ang))
		time.sleep(wait_time)
if __name__ == '__main__':
	GPIO.setmode(GPIO.BOARD) 
	x = Servo(29, "X", 0, 100)
	y = Servo(23, "Y", 0, 100)
	x.turn(0)
	y.turn(0)
	for deg in range(0, 181, 10):
		x.turn(deg, 3)
	y.turn(180)
	GPIO.cleanup()
