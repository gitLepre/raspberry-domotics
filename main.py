#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import Response
import json
import requests
import os 
import RPi.GPIO as GPIO
import time
import Adafruit_DHT


#pins = [7,11,12,13,15,16,18,22,29,31,32,33,37] pin fisici
#pins = [4,17,18,27,22,23,24,25,5,6,12,13,26] #pin codifica BCM

# pins che possiamo utlizzare 17 18 27 22 23 5 6 12

pinsUsabili = [17,18,27,22,23,5,6,12]


#accendo e spengo i led per vedere se il raspberry funziona all'avvio
def powercycle():
    global pinsUsabili

    GPIO.setmode(GPIO.BCM)    #usiamo la numerazione BCM
    GPIO.setwarnings(False)
    for count in range(1,3):
        for item in pinsUsabili:
            GPIO.setup(item,GPIO.OUT)   #imposto Pin 17 ad out, corrispondente al comando: gpio mode 0 out
            GPIO.output(item,GPIO.HIGH)
			
        time.sleep(1)
		
        for item in pinsUsabili:
            GPIO.output(item,GPIO.LOW)  #spengo il led, corrispondente al comando: gpio write 0 0
    
#controlla il token che arriva dal server
def checkToken(token):
    
    tokendata = {"token": token}#dati che passiamo al file php
    resp = requests.post('http://webdev.dibris.unige.it/~S4254186/tesi/php/tokenIsValid.php', data = tokendata)
    r = resp.json()#json di ritorno dal file php
    
    if r["code"] == 0:
       return True #se nel json c'è 0 il token è valido
    else:
        return False




GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Benvenuti in Homer'



@app.route('/gpio', methods = ['POST'])
def accendiLed():
    
    gpio = request.form['gpio']
    token = request.form.get('token')

    GPIO.setup(int(gpio), GPIO.OUT)
    if checkToken(token): 
        if GPIO.input(int(gpio)) == True:
            GPIO.output(int(gpio) , GPIO.LOW)
            return gpio + "spento" 
        else:
            GPIO.output( int(gpio),GPIO.HIGH)
            return gpio + "acceso"
    else:
        return "token sbagliato"
    



@app.route('/gpioOn', methods = ['POST'])
def accendi():
    
    gpio = request.form['gpio']
    token = request.form.get('token')

    GPIO.setup(int(gpio), GPIO.OUT)
    if checkToken(token): 
        GPIO.output( int(gpio),GPIO.HIGH)
        return gpio + "acceso"

    else:
        return "token sbagliato"
    
    
    
    
    
@app.route('/gpioOff', methods = ['POST'])
def spegni():
    
    gpio = request.form['gpio']
    token = request.form.get('token')

    GPIO.setup(int(gpio), GPIO.OUT)
    if checkToken(token): 
        GPIO.output( int(gpio),GPIO.LOW)
        return gpio + "spento"
    else:
        return "token sbagliato"
    
    
    
@app.route('/tuttoOn', methods = ['POST'])
def accendiTutto():
    
    token = request.form.get('token')

    if checkToken(token): 
            for item in pinsUsabili:
                GPIO.setup(item,GPIO.OUT)   
                GPIO.output(item,GPIO.HIGH)

    else:
        return "token sbagliato"
    
    return "ok"



@app.route('/tuttoOff', methods = ['POST'])
def spegniTutto():
    
    token = request.form.get('token')

    if checkToken(token): 
            for item in pinsUsabili:
                GPIO.setup(item,GPIO.OUT)   
                GPIO.output(item,GPIO.LOW)

    else:
        return "token sbagliato"
    
    return "ok"
    

#ritorna file json contenente tutti i gpio accesi
@app.route('/statoGpio', methods = ['POST'])
def stato():
    
    token = request.form.get('token')
    
    if checkToken(token):
        gpioAccesi = []
           
        for value in pinsUsabili:
            GPIO.setup(value, GPIO.OUT)
            if GPIO.input(value) == True:
                gpioAccesi.append(value)
        
        data = {}
        data['gpioAccesi'] = gpioAccesi
        json_data = json.dumps(data)

        return Response(json_data,  mimetype='application/json')
    else:
        return "token errato"
    
    

@app.route('/tokenSensore', methods = ['POST'])
def tokenSensore():
    token = request.form.get('token')

    if(checkToken(token)):
        return "true"
    else:
        return "false"
    
    
#Prende in input un json dove ci sono le regole per il sensore di presenza e ne crea il file
@app.route('/presenza', methods = ['POST'])
def sensorePresenza():
    
    dati = request.get_json()
    with open ('datiPresenza.json','w') as outfile: #creo file json per memorizzarmi le impostazioni, all'acccensione del rasp dovro leggerlo
        json.dump(dati,outfile)
    
    return "ok"

    
#Prende in input un json dove ci sono le regole per il sensore di temperatura e ne crea il file
@app.route('/temperatura', methods = ['POST'])        
def regoleTemperatura():   

    dati = request.get_json()
    with open ('datiTemperatura.json','w') as outfile: #creo il file delle regole e scrivo le regole
        json.dump(dati,outfile)

            
    return "ok"


#ritorna un file json con temperatura e umidita attuale
@app.route('/getTemperatura', methods = ['POST'])        
def getTemperatura():   
    
    pin = 26
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print(round(temperature,1))
    
    data = {}
    data['temperatura'] = round(temperature,1)
    data['umidita'] = round(humidity,1)
    json_data = json.dumps(data)
        
    return Response(json_data,  mimetype='application/json')
    
    
    

@app.route('/seriale/')
def seriale():
# Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

powercycle() 


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True,threaded=True)
#    app.run(host='0.0.0.0', port=80,threaded=True)


         


