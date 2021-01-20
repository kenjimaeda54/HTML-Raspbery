from flask import Flask,render_template

import datetime
import commands
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

estado={'olho_es': False,'olho_dir': False}

olho_esq=20
olho_dir=21

GPIO.setup(olho_esq,GPIO.OUT)
GPIO.setup(olho_dir,GPIO.OUT)
GPIO.output(olho_esq,False)
GPIO.output(olho_dir,False)

@app.route("/")
def inicio():
	return mostra_estado()

@app.route("/olho_esq/1")
def ligar_olho_esq():
	GPIO.output(olho_esq,True)
	return mostra_estado()
@app.route("/olho_esq/0")
def desl_olho_esq():
	GPIO.output(olho_esq,False)
	return mostra_estado()
	
@app.route("/olho_dir/1")
def ligar_olho_dir():
	GPIO.output(olho_dir,True)
	return mostra_estado()
@app.route("/olho_dir/0")
def desl_olho_dir():
	GPIO.output(olho_dir,False)
	return mostra_estado()
def mostra_estado():
	estado={'olho_esq':GPIO.input(olho_esq),
	        'olho_dir':GPIO.input(olho_dir)
	       }
        return render_template('controle-led.html',**estado)
if __name__=="__main__":
   print("Servidor:" +commands.getoutput('hostname-I').strip()+":5000")
app.run(host='0.0.0.0',debug=True)
				
