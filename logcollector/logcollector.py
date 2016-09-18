#! /usr/bin/env python3

import socket
import time
import signal
import sys
import os
import SensorData_pb2

HOST = ""
PORT = 54321

server = None

def signal_handler(signal, frame):
	print('You pressed Ctrl+C!')
	server.close()
	sys.exit(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

signal.signal(signal.SIGINT, signal_handler)

while True:
	serverconn, addr = server.accept()

	print("Accepted!", addr)
	
	msg = SensorData_pb2.SensorDataMessage()
	

	messagebytes = bytearray()
	while True:
		buf = serverconn.recv(4096)
		if not buf:
			break
		messagebytes.extend(buf)
	print(len(messagebytes))
	msg.ParseFromString(bytes(messagebytes))
	
	print(msg.displayname)
	print(msg.sensorname)
	print(len(msg.sensorreading))
	
	if(not os.path.isdir(os.path.join("./data",msg.sensorname))):
		os.makedirs(os.path.join("./data",msg.sensorname))
	
	with open(os.path.join("./data", msg.sensorname, "log-{0}.tsv".format(time.time())), "w") as f:
		print('displayname\ttimestamp\tx\ty\tz', file=f)
		for reading in msg.sensorreading:
			print(msg.displayname, file=f, end="\t")
			print(reading.timestamp, file=f, end="\t")
			print(reading.x, file=f, end="\t")
			print(reading.y, file=f, end="\t")
			print(reading.z, file=f)
	
	serverconn.close()
