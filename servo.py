import time
import RPi.GPIO as GPIO

class Servo:
	def __init__(self, pin_number, name, parent):
		self.name = name
		self.parent = parent
		self.pin_number = pin_number
		print "[!]Servo \"{}\" created on pin: {}".format(self.name, self.pin_number)
        
	def turn(self, ang=180, wait_time=0.5):
		print "[*]Turning {} deg on pin {}".format(ang, self.pin_number)
#		print "[*] Turning {} deg on servo {}, PIN:  {}, DC: {}".format(ang, self.name, self.pin_number)
		self.parent.serial_connection.write("{},{}\n".format(self.pin_number,ang))
		self.parent.serial_connection.flushOutput()
#		print "{},{}\n".format(self.pin_number,ang)
#		x = self.serial.readline()
#		print x
		time.sleep(wait_time)
	def rel_pell(self):
		self.turn(20, 0.5)
		self.turn(0, 0.5)
		
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
