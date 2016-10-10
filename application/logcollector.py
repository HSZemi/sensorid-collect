#! /usr/bin/env python3

import socket
import time
import signal
import sys
import os
import argparse
import SensorData_pb2

server = None
# default host: ""
# default port: 54321

def signal_handler(signal, frame):
	print('\nYou pressed Ctrl+C!\nShutting down.')
	global server
	server.close()
	sys.exit(0)


def main():
	parser = argparse.ArgumentParser(prog='logcollector')
	parser.add_argument('--host', help='select the hostname to bind to', default="")
	parser.add_argument('--port', help='select the port the application shall listen on', default=54321)
	parser.add_argument('target', help='target directory')
	args = parser.parse_args()
	
	if(not os.path.isdir(args.target)):
		print("Error: Target '{}' does not exist".format(args.target))
		sys.exit()
	
	global server
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((args.host, args.port))
	server.listen(1)

	signal.signal(signal.SIGINT, signal_handler)

	# this loop runs until the signal_handler is called and exits the application
	while True:
		serverconn, addr = server.accept()

		print("Accepted:", addr)
		
		msg = SensorData_pb2.SensorDataMessage()
		
		# read the incoming message into messagebytes
		messagebytes = bytearray()
		while True:
			buf = serverconn.recv(4096)
			if not buf:
				break
			messagebytes.extend(buf)
		print(len(messagebytes))
		
		# parse the SensorDataMessage from messagebytes
		msg.ParseFromString(bytes(messagebytes))
		
		# print trivia
		print(msg.displayname)
		print(msg.sensorname)
		print(len(msg.sensorreading))
		
		# create data subdirectory for the sensor (if it does not already exist)
		if(not os.path.isdir(os.path.join(args.target,msg.sensorname))):
			os.makedirs(os.path.join(args.target,msg.sensorname))
		
		# create the tsv file and print the message contents into that file
		with open(os.path.join(args.target, msg.sensorname, "log-{0}.tsv".format(time.time())), "w") as f:
			print('displayname\ttimestamp\tx\ty\tz', file=f)
			for reading in msg.sensorreading:
				print(msg.displayname, file=f, end="\t")
				print(reading.timestamp, file=f, end="\t")
				print(reading.x, file=f, end="\t")
				print(reading.y, file=f, end="\t")
				print(reading.z, file=f)
		
		print("Closing connection.\n")
		serverconn.close()
		# continue the loop and wait for the next incoming connection


if __name__ == "__main__":
    main()
