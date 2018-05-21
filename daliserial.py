import time
import serial
import string
import binascii
import os
from stat import *


try:
	# Name of the file to check.
	fName = "/home/pi/test.txt"

	# Get the time the file was last modified.
	fInfo = os.stat(fName)
	mTime = fInfo[ST_MTIME]
	while True:
		ser = serial.Serial(port='/dev/ttyAMA0', baudrate=19200,
							parity=serial.PARITY_EVEN,
							stopbits=serial.STOPBITS_ONE,
							bytesize=serial.EIGHTBITS
							)
							
		fInfo = os.stat(fName)
		if mTime != fInfo[ST_MTIME]:
			print "File modified"
			mTime = fInfo[ST_MTIME]

			file = open("/home/pi/test.txt", "r")
			dali = file.readline()
			file.close()
		
			ser.write(dali.decode("hex"))
			
			#while True:
			#	if ser.inWaiting() >0:
			#		data = ser.read(12)
			#		print data
			#		time.sleep(1)
	
	
except KeyboardInterrupt, e:
	print "Exiting Program"
		
except:
 print "Error Occurs, Exiting Program bla "
		
finally:
	ser.close()
	pass