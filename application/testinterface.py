#! /usr/bin/env python3

import socket
import time
import signal
import sys
import os
import json

import TestData_pb2
from google.protobuf.internal import encoder
from google.protobuf.internal import decoder

from sklearn import svm
import numpy as np

HOST = ""
PORT = 54322
PATH = "data.old"
GAMMA=0.001
C=100.

SERVER = None

def signal_handler(signal, frame):
	print('You pressed Ctrl+C!')
	global SERVER
	SERVER.close()
	sys.exit(0)

def main():
	normalizeddata = {}
	sensortypes = {}
	with open(os.path.join(PATH, "normalizeddata.json"), "r") as f:
		normalizeddata = json.load(f)
	with open(os.path.join(PATH, "enhancedsensors.json"), "r") as f:
		sensortypes = json.load(f)
		
	classifiers = {}

	for selected_sensor_type in sorted(sensortypes):

		print("Selected sensor type: {0}".format(selected_sensor_type))
		print("Contains {0} sensors: ".format(len(sensortypes[selected_sensor_type])), end="")
		for sensor in sensortypes[selected_sensor_type]:
			print("{0} ({1}), ".format(sensor, sensortypes[selected_sensor_type][sensor]), end="")
		print("")
		
		
		data = np.matrix(normalizeddata[selected_sensor_type]['data'])
		target_sensor_name = np.array(normalizeddata[selected_sensor_type]['target_sensor_name'])
		target_device_id = np.array(normalizeddata[selected_sensor_type]['target_device_id'])

		print("Contains {0} devices: {1}".format(len(set(target_device_id)), ", ".join(set(target_device_id))))
		
		if(len(set(target_device_id)) < 1):
			print("skipping…\n\n")
			continue
	
		#print(data.shape)
		#print(target_sensor_name.shape)
		#print(target_device_id.shape)
		
		classifiers[selected_sensor_type] = svm.SVC(gamma=GAMMA, C=C)
		classifiers[selected_sensor_type].fit(data, target_device_id)
	
	
	global SERVER
	SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	SERVER.bind((HOST, PORT))
	SERVER.listen(1)

	signal.signal(signal.SIGINT, signal_handler)

	while True:
		serverconn, addr = SERVER.accept()

		print("Accepted!", addr)
		
		msg = TestData_pb2.FeatureVector()
		
		messagebytes = bytearray()
		firstloop = True
		size = 0
		position = 0
		received = 0
		while True:
			buf = serverconn.recv(4096)
			
			if(firstloop):
				(size, position) = decoder._DecodeVarint(buf, 0)
				
			received += len(buf)
			
			messagebytes.extend(buf)
			
			if not buf or received >= (position + size):
				break
		print(len(messagebytes))
		msg.ParseFromString(bytes(messagebytes[position:position+size]))
		
		print(msg.sensortype)
		print(msg.sensorname)
		
		feature_vector = [[msg.mean_x, msg.mean_y, msg.mean_z, msg.min_x, msg.min_y, msg.min_z, msg.max_x, msg.max_y, msg.max_z, msg.stddev_x, msg.stddev_y, msg.stddev_z, msg.count]]
		
		prediction = ['NONE']
		if msg.sensortype not in classifiers:
			prediction = ['UNKNOWN_SENSOR_TYPE']
		else:
			prediction = classifiers[msg.sensortype].predict(feature_vector)
		
		print(prediction)
		
		retval = TestData_pb2.TestResult()
		retval.result_displayname = ",".join(prediction)
		
		print("Sending guess: {}".format(retval.result_displayname))
		
		serializedMessage = retval.SerializeToString()
		delimiter = encoder._VarintBytes(len(serializedMessage))
		
		serverconn.sendall((delimiter + serializedMessage))
		
		serverconn.close()

if __name__ == "__main__":
    main()
