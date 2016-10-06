#! /usr/bin/env python3

import json

mydata = {}
mydata['a'] = {}
mydata['b'] = {}
	
with open("../data.set2/measurements.json", "r") as f:
	data = json.load(f)
	for entry in data["Invensense Linear Acceleration"]:
		if entry['deviceid'] not in mydata['a']:
			mydata['a'][entry['deviceid']] = []
		mydata['a'][entry['deviceid']].append(entry['data'])
		
	for entry in data["Invensense Magnetometer"]:
		if entry['deviceid'] not in mydata['b']:
			mydata['b'][entry['deviceid']] = []
		mydata['b'][entry['deviceid']].append(entry['data'])
		

for x in ('a','b'):
	for device in mydata[x]:
		segmentlength = int(len(mydata[x][device]) / 4)
		for i in range(4):
			with open("{}-{}-{}.dat".format(device, i, x), "w") as f:
				print("ts\tx\ty\tz", file=f)
				for j in range(segmentlength*i, segmentlength*(i+1)):
					for line in mydata[x][device][j]:
						print("{0}\t{1}\t{2}\t{3}".format(line['timestamp'], line['x'], line['y'], line['z']), file=f)
