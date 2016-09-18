#! /usr/bin/env python3

import os

data = {}

for folder in os.listdir():
	if(os.path.isdir(folder)):
		data[folder] = []
		for tsv in os.listdir(folder):
			with open(os.path.join(folder, tsv), "r") as f:
				lines = -1
				for line in f:
					lines += 1
				data[folder].append(lines)

print("sensor\ttotalcount\tavg\tmin\tmax")
for key in data:
	print(key, end="\t")
	
	summ = 0
	minn = data[key][0]
	maxx = data[key][0]
	for x in data[key]:
		summ += x
		minn = min(minn, x)
		maxx = max(maxx, x)
	print(summ, end="\t")
	print((summ/len(data[key])), end="\t")
	print(minn, end="\t")
	print(maxx)