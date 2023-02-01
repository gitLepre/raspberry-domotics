#!/usr/bin/python3
import json
import os 
import requests

def getserial():
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

os.system("curl  http://localhost:4040/api/tunnels > tunnels.json") #chiamo api di ngrok e creo tunnel.json

with open('tunnels.json') as data_file: #apro il file e leggo il json    
    datajson = json.load(data_file)


myUrl= datajson['tunnels'][1]['public_url'] #leggo url dal json

id_rasp = getserial()

myData = {"url": myUrl,"id_rasp": id_rasp}#dati che passiamo al file php
resp = requests.post('http://webdev.dibris.unige.it/~S4254186/tesi/php/setMyURL.php', data = myData)


