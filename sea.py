import serial
import time
ser = serial.Serial("/dev/ttyACM0", 9600)
for x in range(0, 181, 10):
	time.sleep(0.5)
	ser.write("1,{}\n".format(x))
for x in range(0, 181, 10):
	time.sleep(0.5)
	ser.write("0,{}\n".format(x))

