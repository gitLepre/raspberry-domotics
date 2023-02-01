#!/usr/bin/python3
import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
import json

#variabili che contengono i dati inviati da app per le regole del sensore di presenza
gpioPresenza = []            
notificaPresenza = "False"
azione = "accendi"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#legge i dati dai file delle regole (presenza e temperatura, varie)
def leggiDati():
    with open ('datiPresenza.json') as jsonfile: 
        d = json.load(jsonfile)
           
    global gpioPresenza
    global notificaPresenza
    global azione
    gpioPresenza = d["gpio"]           
    notificaPresenza = d["notifica"]
    azione = d["azione"]
    
    
def presenza():

    global gpioPresenza
    global notificaPresenza
    global azione
    pir = 13                                         
    GPIO.setup(pir, GPIO.IN)
 
    while True:
    #if not activePres:        
        if GPIO.input(pir): #movimento trovato
            print("Presenza rilevata")
            for value in gpioPresenza:
                GPIO.setup(int(value), GPIO.OUT)
                if azione == "Accendi":
                    GPIO.output(int(value), GPIO.HIGH)
                elif azione == "Spegni":
                    GPIO.output( int(value),GPIO.LOW)
             #if notificaPresenza["notifica"] == "True":  
                #return "bella raga"
            
            time.sleep(3)
        




leggiDati()
presenza()