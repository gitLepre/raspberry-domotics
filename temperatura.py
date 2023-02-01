#!/usr/bin/python3

#git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#cd Adafruit_Python_DHT
#sudo apt-get update
#sudo apt-get install build-essential python-dev python-openssl
#sudo python setup.py install


import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
import json
import sys
import Adafruit_DHT
import json
import os.path


#file json cosi composto

#job = "Accendi"/"Spegni"
#gpio = lista di gpio da attivare
#quando = "Maggiore"/"Minore"
#temperatura = numero intero

gpioTemperatura = []            
job = "Accendi"
quando = "Maggiore"
temperatura = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




#legge i dati dai file delle regole (presenza e temperatura, varie)
def leggiDati():
    with open ('datiTemperatura.json') as jsonfile: 
        d = json.load(jsonfile)
           
    global gpioTemperatura
    global job
    global quando
    global temperatura
    
    
    gpioTemperatura = d["gpio"]           
    temperatura = int(d["temperatura"])
    job = d["job"]
    quando = d["quando"]
 
def sensoreTemperatura():
    
    global gpioTemperatura
    global job
    global quando
    global temperatura
    sensor = Adafruit_DHT.DHT22
    pin = 26
    
    #for setup gpio
    for value in gpioTemperatura:
            GPIO.setup(int(value), GPIO.OUT)
    
    #ultimaModifica = os.path.getmtime('datiTemperatura.json')
    
    while True:
        
        #if(ultimaModifica < os.path.getmtime('datiTemperatura.json')):
            #leggiDati()
            #ultimaModifica = os.path.getmtime('datiTemperatura.json')
            #for value in gpioTemperatura:
                #GPIO.setup(int(value), GPIO.OUT)
                     
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        #print ("Temperatura: ",round(temperature,1), "°C")
        #print ("Umidità percepita: ",round(humidity,1),"%")
        if(quando == "Maggiore" and round(temperature,1) > temperatura or quando == "Minore" and round(temperature,1) < temperatura): 
            for value in gpioTemperatura:
                if(job == "Accendi"):
                    GPIO.output( int(value),GPIO.HIGH)
                elif(job == "Spegni"):
                    GPIO.output( int(value),GPIO.LOW)

        time.sleep(4)


leggiDati()
sensoreTemperatura()