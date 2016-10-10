#! /usr/bin/env python3

import socket
import time
import signal
import sys
import os
import json
import argparse

import TestData_pb2
from google.protobuf.internal import encoder
from google.protobuf.internal import decoder

from sklearn import svm
import numpy as np

GAMMA=0.001
C=100.

server = None
# default host: ""
# default port: 54322

def signal_handler(signal, frame):
	print('\nYou pressed Ctrl+C!\nShutting down.')
	global server
	server.close()
	sys.exit(0)

def main():
	parser = argparse.ArgumentParser(prog='testinterface')
	parser.add_argument('--host', help='select the hostname to bind to', default="")
	parser.add_argument('--port', help='select the port the application shall listen on', default=54322)
	parser.add_argument('--limitfeatures', help='the features used for training and testing', action='store', default=None)
	parser.add_argument('target', help='target directory')
	args = parser.parse_args()
	
	if(not os.path.isdir(args.target)):
		print("Error: Target '{}' does not exist".format(args.target))
		sys.exit()
	
	limitfeatures = None
	if(args.limitfeatures):
		limitfeatures = int(args.limitfeatures)
		if(limitfeatures < 1):
			print("Error: limitfeatures must be > 0")
			sys.exit()
	
	# Read enhanced sensor data and normalized data that have been created by processData.py
	normalizeddata = {}
	sensortypes = {}
	with open(os.path.join(args.target, "normalizeddata.json"), "r") as f:
		normalizeddata = json.load(f)
	with open(os.path.join(args.target, "enhancedsensors.json"), "r") as f:
		sensortypes = json.load(f)
	
	# we will create a classifier for every sensor type in our data
	classifiers = {}

	for selected_sensor_type in sorted(sensortypes):

		print("Selected sensor type: {0}".format(selected_sensor_type))
		print("Contains {0} sensors: ".format(len(sensortypes[selected_sensor_type])), end="")
		for sensor in sensortypes[selected_sensor_type]:
			print("{0} ({1}), ".format(sensor, sensortypes[selected_sensor_type][sensor]), end="")
		print("")
		
		# take the data from normalizeddata
		data = np.matrix(normalizeddata[selected_sensor_type]['data'])
		
		if(limitfeatures and data.shape[1] >= limitfeatures):
			print("Cutting feature vector at {}".format(limitfeatures))
			data = data[:,[i for i in range(limitfeatures)]]
		
		#target_sensor_name = np.array(normalizeddata[selected_sensor_type]['target_sensor_name'])
		target_device_id = np.array(normalizeddata[selected_sensor_type]['target_device_id'])

		print("Contains {0} devices: {1}".format(len(set(target_device_id)), ", ".join(set(target_device_id))))
		
		if(len(set(target_device_id)) < 1):
			print("skipping…\n\n")
			continue
	
		# create and train the classifier
		classifiers[selected_sensor_type] = svm.SVC(gamma=GAMMA, C=C)
		classifiers[selected_sensor_type].fit(data, target_device_id)
	
	
	global server
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((args.host, args.port))
	server.listen(1)

	signal.signal(signal.SIGINT, signal_handler)

	while True:
		serverconn, addr = server.accept()

		print("Accepted:", addr)
		
		msg = TestData_pb2.FeatureVector()
		
		# read the message into messagebytes
		messagebytes = bytearray()
		firstloop = True
		size = 0
		position = 0
		received = 0
		while True:
			buf = serverconn.recv(4096)
			
			# the first bytes tell us how long the actual message will be
			if(firstloop):
				(size, position) = decoder._DecodeVarint(buf, 0)
				
			received += len(buf)
			
			messagebytes.extend(buf)
			
			if not buf or received >= (position + size):
				break
		print(len(messagebytes))
		
		# parse the FeatureVector from messagebytes (without the length)
		msg.ParseFromString(bytes(messagebytes[position:position+size]))
		
		print(msg.sensortype)
		print(msg.sensorname)
		
		# create the (shortened) feature vector from the data in the FeatureVector message
		feature_vector = [[msg.count, msg.mean_x, msg.mean_y, msg.mean_z, msg.min_x, msg.min_y, msg.min_z, msg.max_x, msg.max_y, msg.max_z, msg.stddev_x, msg.stddev_y, msg.stddev_z, msg.avgdev_x, msg.avgdev_y, msg.avgdev_z, msg.skewness_x, msg.skewness_y, msg.skewness_z, msg.kurtosis_x, msg.kurtosis_y, msg.kurtosis_z, msg.rmsamplitude_x, msg.rmsamplitude_y, msg.rmsamplitude_z]]
		
		if(limitfeatures):
			print("Cutting feature vector at {}".format(limitfeatures))
			feature_vector = [feature_vector[0][:limitfeatures]]
		
		prediction = ['NONE']
		if msg.sensortype not in classifiers:
			prediction = ['UNKNOWN_SENSOR_TYPE']
		else:
			# use the precomputed classifier to classify the feature vector
			prediction = classifiers[msg.sensortype].predict(feature_vector)
		
		print(prediction)
		
		# create the TestResult message
		retval = TestData_pb2.TestResult()
		retval.result_displayname = ",".join(prediction)
		
		print("Sending guess: {}".format(retval.result_displayname))
		
		serializedMessage = retval.SerializeToString()
		
		# encode the message length
		delimiter = encoder._VarintBytes(len(serializedMessage))
		
		# send encoding of message length + message back to client
		serverconn.sendall((delimiter + serializedMessage))
		
		serverconn.close()

if __name__ == "__main__":
    main()
