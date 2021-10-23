from flask import Flask, render_template, request
import RPi.GPIO as GPIO
temperature = 0
index = 0
labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

def mydecode(str):
	return str.decode('utf-8')
app = Flask(__name__,template_folder='.')
GPIO.setwarnings(False)
name = "azzedine"
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
	template = {'machines':machines,'labels':labels,'values':values,'max':110,'title':'we fucked up'}
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
	template = {'machines':machines,'bar_labels':labels,'bar_values':values}
	return render_template("index.html", **template)
@app.route('/bar')
def bar():
	bar_labels=labels
	barvalues=values
	return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=barvalues)
def run_my_project():
    app.run()
def update(temp):
	temperature  = temp
	for i in range(11):
		values[11-i] = values[10-i]
	values[0] = temperature
	print(values)
	#print(index)
