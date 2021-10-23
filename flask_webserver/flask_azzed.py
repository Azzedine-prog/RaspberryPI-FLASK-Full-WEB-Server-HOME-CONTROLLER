from flask import Flask, render_template, request
from serial_program import *
import RPi.GPIO as GPIO
temperature = 0
index = 0
labels = [
    '18:16', '18:16', '18:16', '18:16',
    '18:17', '18:17', '18:17', '18:17',
    '18:17', '18:17', '18:17', '18:17'
]

values = [
    26, 27, 25, 24,
    24, 26, 25, 26,
    27, 28, 25, 24
]
humid_values = [
    69, 66, 64, 65,
    63, 66, 66, 64,
    62, 65, 64, 65
]
colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

servo_state = 'OFF'
servo_status = 'ON'
app = Flask(__name__,template_folder='.')
GPIO.setwarnings(False)
name = "azzedine"
distance = 70
car = 1
#to use raspberry pi board pin numbers
GPIO.setmode(GPIO.BCM)
#set up GPIO output channel
pins = [23,24,25]
machines = {'television' : {'name' : 'television','pin' : pins[0],'state' : GPIO.LOW,'status' : 'OFF'}
,'machine a laver' : {'name' : 'machine a laver','pin' : pins[1],'state' : GPIO.LOW,'status' : 'OFF'}
,'lampe1' : {'name' : 'lampe','pin' : pins[2],'state' : GPIO.LOW,'status' : 'OFF'}}
for pin in pins:
	#print(pin)
	GPIO.setup(int(pin),GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)

def set(pin,state):
	GPIO.output(pin,state)
#def reset(pin):
#GPIO.output(pin,GPIO.LOW)
@app.route("/")
def hello():
	template = {'machines':machines,'carman':car,'distanceman':distance,'servo_state':servo_state,'labels':labels,'values':values,'max':110,'title':'temperature','humidvalues':humid_values,'humidtitle':'humidite'}
	return render_template("index.html", **template)
@app.route("/<machine>/<status>")
def hola(machine,status):
	print("hi ",machine)
	if status == "on":
		machines[machine]['status'] = 'ON'
		machines[machine]['state'] = 'OFF'
		set(machines[machine]['pin'],GPIO.HIGH)
		print("status ",machines[machine]['status'],machine)
	else:
		machines[machine]['status'] = 'OFF'
		machines[machine]['state'] = 'ON'
		set(machines[machine]['pin'],GPIO.LOW)
		print("status ",machines[machine]['status'],machine)
	template = {'machines':machines,'carman':car,'distanceman':distance,'servo_state':servo_state,'labels':labels,'values':values,'max':110,'title':'temperature','humidvalues':humid_values,'humidtitle':'humidite'}
	return render_template("index.html", **template)
@app.route("/servo/<servo_stat>")
def servogarage(servo_stat):
	#print("hi ",machine)
	if servo_stat == "on":
		servo_status = 'OFF'
		servo_state = 'ON'
		write_commande('o')	
		print("status : ",servo_status)
	else:
		servo_status = 'ON'
		servo_state = 'OFF'
		write_commande('f')
		print("status : ",servo_status)
	template = {'machines':machines,'carman':car,'distanceman':distance,'servo_state':servo_state,'labels':labels,'values':values,'max':110,'title':'temperature','humidvalues':humid_values,'humidtitle':'humidite'}
	return render_template("index.html", **template)
@app.route('/bar')
def bar():
	bar_labels=labels
	barvalues=values
	template = {'machines':machines,'distanceman':distance,'carman':car,'servo_state':servo_state,'labels':labels,'values':values,'max':110,'title':'temperature','humidvalues':humid_values,'humidtitle':'humidite'}
def run_my_project():
    app.run(host="0.0.0.0",port=8080)
def update(temp,dist,humid):
	"""temperature  = temp
	global car
	global distance
	for i in range(11):
		values[11-i] = values[10-i]
	values[0] = temperature
	for i in range(11):
		humid_values[11-i] = humid_values[10-i]
	humid_values[0] = humid"""
	"""if dist != 0:
		distance = dist
		if distance > 20:
			car = 1
		else:
			car = 0"""
	print(distance)
	print(car)
	#print(temp)		
	#print(values)
	#print(index)
