import time
import string
import os
#import unhexlify
val = 4

while val != 0:
	

	#os.system('clear')
	print ("Dali ljosa styring")
	print ("Veldu adgerd")
	print ("1. Ljos i fullan styrk")
	print ("2. Ljos i lagmarks styrk")
	print ("3. Ljos slokkt")
	print ("0. loka forriti")

	val = input('Sladu inn adgerd [1-2-3] : ')
	val = int(val)

	if val==1:
		command = '0130313030313046463035454117'
		print "Ljos i fullan styrk"
		time.sleep(1)
		
	if val==2:
		command = '0130313030313046463036453917'
		print "Ljos i lagmarks styrk"
		time.sleep(1)

	if val==3:
		command = '0130313030313046463030454617'
		print "Ljos slokkt"
		time.sleep(1)
		
	if val==0:
		print("Loka forriti")
		time.sleep(1)
		break

	file = open("test.txt", "w")
	file.write(command)
	#file.write(str(pin)+"\n")
	file.close()
						
	#ser.setDTR(True)
	#time.sleep(3)
	#file = open("test.txt", "r")
	#dali = file.readline()
	file.close()
	#dali = '0130313030313046463035454117'
#	try:
#		ser.write(dali.decode("hex"))
		#print "Ljos i max"
#		while True:
#			if ser.inWaiting() >0:
#				data = ser.read(12)
#				print data
#				time.sleep(1)
#				break

				
#	except KeyboardInterrupt:
#		print "Exiting Program"
		
#	except:
#		print "Error Occurs, Exiting Program"
		
#	finally:
#		ser.close()
#		pass