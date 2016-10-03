#! /usr/bin/env python3

import sys
import argparse
import json
import os
import csv
from features import *


def classes(directory):
	sensors = {}

	sensors['TYPE_ACCELEROMETER'] = []
	sensors['TYPE_ACCELEROMETER'].append('BMA150 3-axis Accelerometer')
	sensors['TYPE_ACCELEROMETER'].append('Invensense Accelerometer')
	sensors['TYPE_ACCELEROMETER'].append('Invensense Accelerometer -Wakeup Secondary')
	sensors['TYPE_ACCELEROMETER'].append('LGE Accelerometer Sensor')
	sensors['TYPE_ACCELEROMETER'].append('MPU-6050 Accelerometer')
	sensors['TYPE_ACCELEROMETER'].append('BMI160 accelerometer')
	sensors['TYPE_GRAVITY'] = []
	sensors['TYPE_GRAVITY'].append('Gravity')
	sensors['TYPE_GRAVITY'].append('Gravity Sensor')
	sensors['TYPE_GRAVITY'].append('Invensense Gravity')
	sensors['TYPE_GRAVITY'].append('Invensense Gravity-Wakeup Secondary')
	sensors['TYPE_GYROSCOPE'] = []
	sensors['TYPE_GYROSCOPE'].append('Invensense Gyroscope')
	sensors['TYPE_GYROSCOPE'].append('Invensense Gyroscope -Wakeup Secondary')
	sensors['TYPE_GYROSCOPE'].append('Invensense Gyroscope Uncalibrated')
	sensors['TYPE_GYROSCOPE'].append('Invensense Gyroscope Uncalibrated -Wakeup Secondary')
	sensors['TYPE_GYROSCOPE'].append('LGE Gyroscope Sensor')
	sensors['TYPE_GYROSCOPE'].append('MPU-6050 Gyroscope')
	sensors['TYPE_GYROSCOPE'].append('BMI160 gyroscope (uncalibrated)')
	sensors['TYPE_GYROSCOPE'].append('BMI160 gyroscope')
	sensors['TYPE_LIGHT'] = []
	sensors['TYPE_LIGHT'].append('CM3602 Light sensor')
	sensors['TYPE_LIGHT'].append('Invensense Light')
	sensors['TYPE_LIGHT'].append('Invensense Light -Wakeup Secondary')
	sensors['TYPE_LIGHT'].append('LGE Light Sensor')
	sensors['TYPE_LINEAR_ACCELERATION'] = []
	sensors['TYPE_LINEAR_ACCELERATION'].append('Invensense Linear Acceleration')
	sensors['TYPE_LINEAR_ACCELERATION'].append('Invensense Linear Acceleration-Wakeup Secondary')
	sensors['TYPE_LINEAR_ACCELERATION'].append('Linear Acceleration')
	sensors['TYPE_LINEAR_ACCELERATION'].append('Linear Acceleration Sensor')
	sensors['TYPE_MAGNETIC_FIELD'] = []
	sensors['TYPE_MAGNETIC_FIELD'].append('AK8973 3-axis Magnetic field sensor')
	sensors['TYPE_MAGNETIC_FIELD'].append('ALPS 3-axis Magnetic field sensor')
	sensors['TYPE_MAGNETIC_FIELD'].append('Invensense Magnetometer')
	sensors['TYPE_MAGNETIC_FIELD'].append('Invensense Magnetometer -Wakeup Secondary')
	sensors['TYPE_MAGNETIC_FIELD'].append('Invensense Magnetometer Uncalibrated')
	sensors['TYPE_MAGNETIC_FIELD'].append('Invensense Magnetometer Uncalibrated -Wakeup Secondary')
	sensors['TYPE_MAGNETIC_FIELD'].append('LGE Magnetometer Sensor')
	sensors['TYPE_MAGNETIC_FIELD'].append('BMM150 magnetometer (uncalibrated)')
	sensors['TYPE_MAGNETIC_FIELD'].append('BMM150 magnetometer')
	sensors['TYPE_ORIENTATION'] = []
	sensors['TYPE_ORIENTATION'].append('AK8973 Orientation sensor')
	sensors['TYPE_ORIENTATION'].append('Game Rotation Vector')
	sensors['TYPE_ORIENTATION'].append('Invensense Orientation')
	sensors['TYPE_ORIENTATION'].append('Invensense Orientation-Wakeup Secondary')
	sensors['TYPE_ORIENTATION'].append('Orientation')
	sensors['TYPE_ORIENTATION'].append('Orientation Sensor')
	sensors['TYPE_PRESSURE'] = []
	sensors['TYPE_PRESSURE'].append('Invensense Barometer')
	sensors['TYPE_PRESSURE'].append('Invensense Barometer -Wakeup Secondary')
	sensors['TYPE_PRESSURE'].append('LGE Barometer Sensor')
	sensors['TYPE_PRESSURE'].append('BMP280 pressure')
	sensors['TYPE_PROXIMITY'] = []
	sensors['TYPE_PROXIMITY'].append('CM3602 Proximity sensor')
	sensors['TYPE_PROXIMITY'].append('GP2A - Proximity Sensor')
	sensors['TYPE_PROXIMITY'].append('Invensense Proximity')
	sensors['TYPE_PROXIMITY'].append('Invensense Proximity:Non Wakeup Secondary')
	sensors['TYPE_PROXIMITY'].append('LGE Proximity Sensor')
	sensors['TYPE_ROTATION_VECTOR'] = []
	sensors['TYPE_ROTATION_VECTOR'].append('Game Rotation Vector')
	sensors['TYPE_ROTATION_VECTOR'].append('Geomagnetic Rotation Vector')
	sensors['TYPE_ROTATION_VECTOR'].append('Invensense Game Rotation Vector')
	sensors['TYPE_ROTATION_VECTOR'].append('Invensense Game Rotation Vector-Wakeup Secondary')
	sensors['TYPE_ROTATION_VECTOR'].append('Invensense Geomagnetic Rotation Vector')
	sensors['TYPE_ROTATION_VECTOR'].append('Invensense Geomagnetic Rotation Vector-Wakeup Secondary')
	sensors['TYPE_ROTATION_VECTOR'].append('Invensense Rotation Vector')
	sensors['TYPE_ROTATION_VECTOR'].append('Invensense Rotation Vector-Wakeup Secondary')
	sensors['TYPE_ROTATION_VECTOR'].append('Rotation Vector')
	sensors['TYPE_ROTATION_VECTOR'].append('Rotation Vector Sensor')
	sensors['TYPE_UNKNOWN'] = []
	sensors['TYPE_UNKNOWN'].append('Device Position Classifier')
	sensors['TYPE_UNKNOWN'].append('Invensense Significant Motion Detector')
	sensors['TYPE_UNKNOWN'].append('Invensense Step Counter')
	sensors['TYPE_UNKNOWN'].append('Invensense Step Counter-Wakeup Secondary')
	sensors['TYPE_UNKNOWN'].append('Invensense Step Detector')
	sensors['TYPE_UNKNOWN'].append('Invensense Step Detector-Wakeup Secondary')
	sensors['TYPE_UNKNOWN'].append('Invensense Tilt')
	sensors['TYPE_UNKNOWN'].append('Significant Motion')
	
	with open(os.path.join(directory, 'sensortypes.json'), "w") as f:
		print(json.dumps(sensors), file=f)

def unify(directory):
	alldata = {}

	for element in os.listdir(directory):
		if(os.path.isdir(os.path.join(directory, element))):
			print("reading", element)
			alldata[element] = []
			for f in os.listdir(os.path.join(directory, element)):
				print("opening", f)
				with open(os.path.join(directory, element, f), "r") as inp:
					csvfile = csv.DictReader(inp, delimiter="\t")
					data = []
					deviceid = ''
					for row in csvfile:
						localdict = {}
						for key in ('timestamp','x','y','z'):
							localdict[key] = float(row[key])
						data.append(localdict)
						deviceid = row['displayname']
					if(len(data) > 0):
						ts0 = data[0]['timestamp']
						for localdict in data:
							localdict['timestamp'] -= ts0
						alldata[element].append({'deviceid':deviceid, 'data':data})

	with open(os.path.join(directory, "measurements.json"), "w") as f:
		json.dump(alldata, f)


def extract(directory):
	alldata = {}
	sensortypes = {}

	with open(os.path.join(directory, "measurements.json"), "r") as f:
		alldata = json.load(f)
	with open(os.path.join(directory, "sensortypes.json"), "r") as f:
		sensortypes = json.load(f)

	normalizeddata = {}
	to_delete = []
	for sensortype in sensortypes:
		normalizeddata[sensortype] = {'data':[],'target_sensor_name':[], 'target_device_id':[]}
		newsensorlist = {}
		for sensorname in sensortypes[sensortype]:
			totalcount = 0
			if(sensorname in alldata):
				for measurement in alldata[sensorname]:
					
					meann = {}
					minn = {}
					maxx = {}
					stddevv = {}
					avgdevv = {}
					skewnesss = {}
					kurtosiss = {}
					rmsamplitudee = {}
					
					for index in ('x','y','z'):
					
						meann[index] = mean(measurement['data'], index)
						minn[index] = lowest(measurement['data'], index)
						maxx[index] = highest(measurement['data'], index)
						stddevv[index] = stddev(measurement['data'], index, meann[index])
						avgdevv[index] = avgdev(measurement['data'], index, meann[index])
						skewnesss[index] = skewness(measurement['data'], index, meann[index], stddevv[index])
						kurtosiss[index] = kurtosis(measurement['data'], index, meann[index], stddevv[index])
						rmsamplitudee[index] = rmsamplitude(measurement['data'], index,)
					
					#normalizeddata[sensortype]['data'].append([meann['x'], meann['y'], meann['z'], minn['x'], minn['y'], minn['z'], maxx['x'], maxx['y'], maxx['z'], stddevv['x'], stddevv['y'], stddevv['z'], avgdevv['x'], avgdevv['y'], avgdevv['z'], skewnesss['x'], skewnesss['y'], skewnesss['z'], kurtosiss['x'], kurtosiss['y'], kurtosiss['z'], rmsamplitudee['x'], rmsamplitudee['y'], rmsamplitudee['z'], len(measurement['data']) ])
					normalizeddata[sensortype]['data'].append([meann['x'], meann['y'], meann['z'], minn['x'], minn['y'], minn['z'], maxx['x'], maxx['y'], maxx['z'], stddevv['x'], stddevv['y'], stddevv['z'], len(measurement['data']) ])
					#normalizeddata[sensortype]['data'].append([mean_x, mean_y, mean_z, max_x, max_y, max_z, min_x, min_y, min_z, var_x, var_y, var_z, count])
					#normalizeddata[sensortype]['data'].append([mean_x, mean_y, mean_z])
					normalizeddata[sensortype]['target_sensor_name'].append(sensorname)
					normalizeddata[sensortype]['target_device_id'].append(measurement['deviceid'])
					totalcount += len(measurement['data'])
				newsensorlist[sensorname] = totalcount
			else:
				to_delete.append(sensorname)
		sensortypes[sensortype] = newsensorlist
				
					
	with open(os.path.join(directory, "enhancedsensors.json"), "w") as f:
		json.dump(sensortypes, f)
	with open(os.path.join(directory, "normalizeddata.json"), "w") as f:
		json.dump(normalizeddata, f)

def main():

	parser = argparse.ArgumentParser(prog='processData')

	parser.add_argument('-c', '--classes', help='create sensor classes metafile', action='store_true')
	parser.add_argument('-u', '--unify', help='bring it into a nice format', action='store_true')
	parser.add_argument('-x', '--extract', help='extract feature matrix', action='store_true')
	parser.add_argument('-a', '--all', help='combination of classes, unify and extract', action='store_true')
	parser.add_argument('target', help='target directory')
	args = parser.parse_args()


	if(not os.path.isdir(args.target)):
		print("Error: Target '' does not exist".format(args.target))
		sys.exit()
	
	if(args.classes):
		classes(args.target)
	
	if(args.unify):
		if not os.path.isfile(os.path.join(args.target, 'sensortypes.json')):
			classes(args.target)
		unify(args.target)
	
	if(args.extract):
		if not os.path.isfile(os.path.join(args.target, 'sensortypes.json')):
			classes(args.target)
		if not os.path.isfile(os.path.join(args.target, 'measurements.json')):
			unify(args.target)
		extract(args.target)
		
	if(args.all):
		classes(args.target)
		unify(args.target)
		extract(args.target)
	
if __name__ == "__main__":
    main()