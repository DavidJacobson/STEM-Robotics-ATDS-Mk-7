import time
import RPi.GPIO as GPIO

class Servo:
	def __init__(self, pin_number, name):
		self.name = name
		self.pin_number = pin_number	
		GPIO.setup(pin_number, GPIO.OUT)
		self.p = GPIO.PWM(pin_number, 50)
		self.p.start(2.5)
		print "[!]Servo \"{}\" created on pin: {}".format(self.name, self.pin_number)
        def turn(self, ang=180, wait_time=1):
		print "[*] Turning {} deg on servo {}".format(ang, self.name)
		DC = float(ang) / 10.0 + 2.5
                self.p.ChangeDutyCycle(DC)
		time.sleep(wait_time)
	def stop(self):
		self.p.stop()


if __name__ == '__main__':
	GPIO.setmode(GPIO.BOARD) 
	x = Servo(7)
	x.turn()
