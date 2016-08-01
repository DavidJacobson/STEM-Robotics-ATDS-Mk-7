import time
import RPi.GPIO as GPIO

class Servo:
	def __init__(self, pin_number, name, deg, freq):
		self.name = name
		self.on = True
		self.freq = freq
		self.pin_number = pin_number	
		GPIO.setup(self.pin_number, GPIO.OUT)
		self.p = GPIO.PWM(self.pin_number, self.freq)
		self.p.start(self.ang_to_dc(deg))
		print "[!]Servo \"{}\" created on pin: {}".format(self.name, self.pin_number)
        
	def ang_to_dc(self, ang):
		return (float(ang) / 10.0) + 2.5
	def turn(self, ang=180, wait_time=1):
		DC = self.ang_to_dc(ang)
		print "[*] Turning {} deg on servo {}, PIN:  {}, DC: {}".format(ang, self.name, self.pin_number, DC)
		print self.on
		if self.on:
			self.p.ChangeDutyCycle(DC)
		else:
			self.p.start(DC)
			self.on = True
		time.sleep(wait_time)
	def stop(self):
		self.p.stop()
		self.on = False
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
