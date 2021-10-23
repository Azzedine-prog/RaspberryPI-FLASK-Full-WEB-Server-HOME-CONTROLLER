fil = "flask_azzed.py"
try:
	f = open(fil,"r")
except:
	print("error in opening file")
s = f.read()
f.close()
s = s.decode('utf-8')
#s = s.encode('utf-16')
#s = s.decode('utf-16')
#s = s.encode('ascii')
fil = "new_"+fil
f = open(fil,"w")
f.write(s)
f.close()
