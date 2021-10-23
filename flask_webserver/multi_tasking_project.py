import threading
import serial
import time as t
from serial_program import *
from flask_azzed import *
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()
timeout = 2

def serial(num):
	temp = 0
	luminosite = 0
	humidite = 0
	while True :
		t.sleep(0.5)
		temp = get_temperature()[0]
		print(temp)
def server_gpio(num):
    run_my_project()
  
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
  
    # both threads completely executed
    print("Done!")
