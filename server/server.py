import jsonsocket
import json
import datetime

FILE='sensorData.json'

HOST='0.0.0.0'
PORT=2320

server = Server(HOST, PORT)
dataFile = open(FILE, 'w')
while True:
    server.accept()
    data = server.recv()
    server.send({'status': 'ok'})

    data['timestamp']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

dataFile.close()
