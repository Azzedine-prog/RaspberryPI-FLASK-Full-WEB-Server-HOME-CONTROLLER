import threading
import serial
import time as t
from serial_program import *
from flask_azzed import *
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()
timeout = 2
def serial(num):
	index = 0
	try:
		temp = 0
		luminosite = 0
		humidite = 0
		dist = 0
		while True :
			t.sleep(0.5)
			m = get_values()
			temp = m[0]
			dist = m[1]
			humidite = m[3] 
			update(temp,dist,humidite)
			#print(temp)
	except KeyboardInterrupt:
		print("you dare to kill me mdafaka from serial process\n")
		quit()
def server_gpio(num):
	try:
		run_my_project()
	except KeyboardInterrupt:
		print("you dare to kill me mdafaka from flask process\n")
		quit()

if __name__ == "__main__":
	# creating thread
	t1 = threading.Thread(target=serial, args=(10,))
	t2 = threading.Thread(target=server_gpio, args=(10,))
	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()
	
	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()
	print("interrupted by keyboard\n")
	quit()
	# both threads completely executed
	print("Done!")
