import time
import RPi.GPIO as GPIO

class Servo:
	def __init__(self, pin_number):
		self.pin_number = pin_number	
		GPIO.setup(pin_number, GPIO.OUT)
		self.p = GPIO.PWM(pin_number, 50)
		self.p.start(7.5)
	def sweep(self):
		while True:
			self.p.ChangeDutyCycle(7.5)	
			time.sleep(1)

        def turn(self):
                while True:     
                	for dc in range(0, 101, 5):
            			self.p.ChangeDutyCycle(dc)
            			time.sleep(0.1)
        		for dc in range(100, -1, -5):
            			self.p.ChangeDutyCycle(dc)
            			time.sleep(0.1)


	def stop(self):
		self.p.stop()


if __name__ == '__main__':
	GPIO.setmode(GPIO.BOARD) 
	x = Servo(7)
	x.turn()
