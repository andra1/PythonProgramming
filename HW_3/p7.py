import math

def max(x):
	maximum = x[0]
	for i in range(0,len(x)):
		if x[i] > maximum:
			maximum = x[i]

	return maximum

def min(x):
	minimum = x[0]
	for i in range(0,len(x)):
		if x[i] < minimum:
			minimum = x[i]

	return minimum

def mean(x):
	summation = 0
	for y in x:
		summation = summation + y

	average = float(summation)/ len(x)
	return average

def median(x):
	x = sorted(x)
	if len(x) % 2 == 0:
		middle = math.floor(len(x)/2)
		median = (x[middle] + x[middle-1])/2
		return median

	elif len(x) == 1:
		return x

	else:
		middle = math.floor(len(x)/2)
		median = x[middle]
		return median

def variance(x):
	average = mean(x)
	total_diff = 0
	for y in x:
		total_diff = total_diff + (y-average)**2
	var = float(total_diff)/len(x)
	return var

def summary_statistics(x, function):
	return function(x)

#x = summary_statistics([1,2,3], variance)
#print(x)