# taken from the AccelPrint article

def mean(data, index):
	m = 0
	for x in data:
		m += x[index]
	return ( m / len(data) )

def stddev(data, index, mean):
	val = 0
	for x in data:
		val += pow((x[index] - mean), 2)
	val /= max(len(data)-1, 1)
	return pow(val, 0.5)

def avgdev(data, index, mean):
	val = 0
	for x in data:
		val += abs(x[index] - mean)
	return ( val / len(data) )

def skewness(data, index, mean, stddev):
	if(stddev == 0):
		return 0
	val = 0
	for x in data:
		val += pow(((x[index] - mean)/stddev), 3)
	return ( val / len(data) )

def kurtosis(data, index, mean, stddev):
	if(stddev == 0):
		return 0
	val = 0
	for x in data:
		val += (pow(((x[index] - mean)/stddev), 4) - 3)
	return ( val / len(data) )

def rmsamplitude(data, index):
	val = 0
	for x in data:
		val += pow(x[index], 2)
	val /= len(data)
	return pow(val, 0.5)

def lowest(data, index):
	l = data[0][index]
	for x in data:
		l = min(l, x[index])
	return l

def highest(data, index):
	h = data[0][index]
	for x in data:
		h = max(h, x[index])
	return h