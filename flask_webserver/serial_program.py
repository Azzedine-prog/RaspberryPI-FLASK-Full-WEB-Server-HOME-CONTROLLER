import serial
import time as t
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()
timeout = 5
#line = ""
def get_line():
	t.sleep(0.5)
	#global line
	line = None
	while(line == None):
		if ser.in_waiting > 0:
			#line = ser.readline().decode('utf-8').rstrip()
			line = ser.readline()
	s = str(line).replace('b\'','')
	s = s.replace('\\r\\n\'','')
	return s
def get_values():
	ti = t.time()
	temp = 0
	dist = 0
	luminosite = 0
	humidite = 0
	while (dist == 0 or temp == 0 or humidite == 0 or luminosite == 0) and t.time()-ti < timeout:
		v = get_line()
		array = v.split('=')
		if array[0] == "distance":
			dist = int(array[1])
		elif array[0] == "temperature":
			temp = int(array[1])
		elif array[0] == "luminosite":
			luminosite = int(array[1])
		elif array[0] == "humidite":
			humidite = int(array[1])
		#print(v)
	#print("temp")
	#print(temp)
	return [temp,dist,luminosite,humidite]
def write_commande(commande):
	ser.write(bytes(str(commande),'ascii'))

