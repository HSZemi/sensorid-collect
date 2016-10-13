#! /usr/bin/env python3

from sklearn import svm
import numpy as np
import json
import random
import sys
import os
import argparse

def estimate(data, target, trainingsubset, testingsubset, gamma='auto', C=1):
	if(len(set(target)) < 2): # only one class
		return 0;
	clf = svm.SVC(gamma=gamma, C=C)
	clf.fit(data[trainingsubset], target[trainingsubset])
	prediction = clf.predict(data[testingsubset])
	
	results = zip(prediction, target[testingsubset])
	
	matches = 0
	total = 0
	
	for p, t in results:
		total += 1
		if p == t:
			matches += 1
	
	return matches/total

def successrate_stats(successrates):
	successrate_avg = 0
	successrate_min = successrates[0]
	successrate_max = successrates[0]
	for rate in successrates:
		successrate_avg += rate
		successrate_min = min(rate, successrate_min)
		successrate_max = max(rate, successrate_max)
	successrate_avg /= len(successrates)
	return (successrate_min, successrate_max, successrate_avg)

def successrate_cdf(successrates):
	# create dict with x:0 for x in {0..100}
	cdf = dict(enumerate([0 for i in range(101)]))
	for x in successrates:
		cdf[int(x*100)] += 1
	for key in range(1,101):
		cdf[key] += cdf[key-1]
	return cdf


def main():
	parser = argparse.ArgumentParser(prog='testData')

	parser.add_argument('--default-training-size', help='set the default size of the training set. True size will be min(default_training_size, len(data)-1).', action='store', default=5)
	parser.add_argument('--limittraining', help='limit where training data may come from, e.g. a value of 0.5 limits training data to the first half of the dataset.', action='store', default=1.0)
	parser.add_argument('--limitfeatures', help='the features used for training and testing', action='store', default=None)
	parser.add_argument('--csv', help='write data to csv file', action='store')
	parser.add_argument('--cdf', help='write cdf data to file', action='store')
	parser.add_argument('-s', '--silent', help='do not output anything except errors', action='store_true')
	parser.add_argument('target', help='target directory')
	args = parser.parse_args()

	silent = args.silent
	
	if(not os.path.isdir(args.target)):
		print("Error: Target '{}' does not exist".format(args.target))
		sys.exit()
	
	limittraining = float(args.limittraining)
	if (limittraining < 0) or (limittraining > 1):
		print("Error: limittraining must be between 0 and 1")
		sys.exit()
	
	default_training_size = float(args.default_training_size)
	if default_training_size < 0:
		print("Error: default_training_size must be >= 0")
		sys.exit()
	
	limitfeatures = None
	if(args.limitfeatures):
		limitfeatures = int(args.limitfeatures)
		if(limitfeatures < 1):
			print("Error: limitfeatures must be > 0")
			sys.exit()
	
	
	normalizeddata = {}
	sensortypes = {}

	with open(os.path.join(args.target, "normalizeddata.json"), "r") as f:
		normalizeddata = json.load(f)
	with open(os.path.join(args.target, "enhancedsensors.json"), "r") as f:
		sensortypes = json.load(f)
	
	f = None
	if(args.csv):
		f = open(args.csv, "w")
		print("sensor type\t# sensors\t# devices\tmin\tmax\tavg", file=f)
	
	cdf_data = {}

	for selected_sensor_type in sorted(sensortypes):
		if not silent:
			print("Selected sensor type: {0}".format(selected_sensor_type))
			print("Contains {0} sensors: ".format(len(sensortypes[selected_sensor_type])), end="")
			for sensor in sensortypes[selected_sensor_type]:
				print("{0} ({1}), ".format(sensor, sensortypes[selected_sensor_type][sensor]), end="")
			print("")
		
		
		data = np.matrix(normalizeddata[selected_sensor_type]['data'])
		
		if(limitfeatures and data.shape[1] >= limitfeatures):
			if not silent:
				print("Cutting feature vector at {}".format(limitfeatures))
			data = data[:,[i for i in range(limitfeatures)]]
		
		target_sensor_name = np.array(normalizeddata[selected_sensor_type]['target_sensor_name'])
		target_device_id = np.array(normalizeddata[selected_sensor_type]['target_device_id'])
		
		if not silent:
			print("Contains {0} devices: {1}".format(len(set(target_device_id)), ", ".join(set(target_device_id))))
		
		if(len(set(target_device_id)) < 1):
			if not silent:
				print("\n")
			continue
	
		#print(data.shape)
		#print(target_sensor_name.shape)
		#print(target_device_id.shape)
		
		#successrates_sensor = []
		successrates_device = []
		#successrates_device2 = []
		upper_training_limit = limittraining * data.shape[0]
		training_size = int(min(default_training_size, upper_training_limit, (data.shape[0]-1 / len(set(target_device_id)))))
		if(default_training_size < 1):
			training_size = int(min(data.shape[0] * default_training_size, upper_training_limit, data.shape[0]-1))

		for i in range(100):
			completeset = set(range(data.shape[0]))
			trainingsubset = set()
			
			for deviceid in set(target_device_id):
				device_training_set = set()
			
				while(len(device_training_set) < training_size):
					index = random.randrange(0, upper_training_limit)
					if(target_device_id[index] == deviceid):
						device_training_set.add(index)
				trainingsubset |= device_training_set
				
			testingsubset = completeset - trainingsubset

			trainingsubset = list(trainingsubset)
			testingsubset = list(testingsubset)

			#print(target_device_id[trainingsubset])
			#successrates_sensor.append(estimate(data, target_sensor_name, trainingsubset, testingsubset))
			successrates_device.append(estimate(data, target_device_id, trainingsubset, testingsubset))
			#successrates_device2.append(estimate(data, target_device_id, trainingsubset, testingsubset, gamma=0.001, C=100.))
		
		
		#sr_min, sr_max, sr_avg = successrate_stats(successrates_sensor)
		
		#print("Success rate (Sensor): min {0:.2f} / max {1:.2f} / avg {2:.2f}".format(sr_min, sr_max, sr_avg))
		if not silent:
			print("Training: {} values per device; Testing: {} values per device".format(training_size, (data.shape[0]-(training_size * len(set(target_device_id))) / len(set(target_device_id)))))
		
		sr_min, sr_max, sr_avg = successrate_stats(successrates_device)
		cdf = successrate_cdf(successrates_device)
		cdf_data[selected_sensor_type] = cdf
		if not silent:
			print("Success rate (Device): min {0:.2f} / max {1:.2f} / avg {2:.2f}".format(sr_min, sr_max, sr_avg))
		
			print("\n")
		
		if(args.csv):
			print("{}\t{}\t{}\t{}\t{}\t{}".format(
				selected_sensor_type, 
				len(sensortypes[selected_sensor_type]),
				len(set(target_device_id)),
				sr_min,
				sr_max,
				sr_avg,
			), file=f)
	
	if(args.cdf):
		with open(args.cdf, "w") as f:
			for index in sorted(cdf_data):
				print(index, end="\t", file=f)
			print("", file=f)
			for i in range(101):
				for index in sorted(cdf_data):
					print(cdf_data[index][i], end="\t", file=f)
				print("", file=f)
	
	
if __name__ == "__main__":
    main()
