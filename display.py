### This file is the class for the 7-seg display
import time
import RPi.GPIO as GPIO

class Display:

	def __init__(self, SDI, RCLK, SRCLK):
		self.SDI = SDI
		self.RCLK = RCLK
		self.SRCLK = SRCLK
	        GPIO.setup(SDI, GPIO.OUT)
       		GPIO.setup(RCLK, GPIO.OUT)
        	GPIO.setup(SRCLK, GPIO.OUT)
        	GPIO.output(SDI, GPIO.LOW)
        	GPIO.output(RCLK, GPIO.LOW)
        	GPIO.output(SRCLK, GPIO.LOW)
		self.hex_vals = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f] #plz work
	def reg_shift(self, dat): # Not our code, we can't be blamed...
        	for bit in range(0, 8):
                	GPIO.output(self.SDI, 0x80 & (dat << bit))
                	GPIO.output(self.SRCLK, GPIO.HIGH)
                	time.sleep(0.001)
                	GPIO.output(self.SRCLK, GPIO.LOW)
        	GPIO.output(self.RCLK, GPIO.HIGH)
        	time.sleep(0.001)
        	GPIO.output(self.RCLK, GPIO.LOW)
	def disp_val(self, val):
		self.reg_shift(self.hex_vals[val])
		time.sleep(0.1)		
