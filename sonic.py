# This is the file for the Sonic class
import RPi.GPIO as GPIO
import time

class Sonic:

	def __init__(self, TRIGGER, ECHO):
		self.TRIGGER = TRIGGER
		self.ECHO = ECHO
		
		GPIO.setup(TRIGGER,GPIO.OUT)
		GPIO.setup(ECHO,GPIO.IN)


	def get_dist(self):
		"""This method takes no arugments, and returns the distance to an object if one exists, if not it returns None"""
		while True:

		  GPIO.output(self.TRIGGER, False)                 #Set TRIG as LOW
		  print "Waitng For Sensor To Settle"
		  time.sleep(1)                            #Delay of 2 seconds

		  GPIO.output(self.TRIGGER, True)                  #Set self.TRIGGER as HIGH
		  time.sleep(0.00001)                      #Delay of 0.00001 seconds
		  GPIO.output(self.TRIGGER, False)                 #Set self.TRIGGER as LOW

		  while GPIO.input(self.ECHO)==0:               #Check whether the self.ECHO is LOW
			pulse_start = time.time()              #Saves the last known time of LOW pulse

		  while GPIO.input(self.ECHO)==1:               #Check whether the self.ECHO is HIGH
			pulse_end = time.time()                #Saves the last known time of HIGH pulse 

		  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

		  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
		  distance = round(distance, 2)            #Round to two decimal points

		  if distance > 2 and distance < 400:      #Check whether the distance is within range
			print "[!] Object {} CM away".format(distance)
			return distance - 0.5  #Print distance with 0.5 cm calibration
		  else:
			print "[*] No object found"
			return None                   #display out of range



