import math


#converts all the user input into a list of lists
def convert_to_list(text):
	clean = []
	for item in collection:
		item = item.split(",")
		item = [int(x) for x in item]
		clean.append(item)
	return clean



#function to calculate distance between two points in n dimensional space and return a float value
def distance(data, reference):
	origin = [0,0]
	dimension = len(data)
	summation  = 0
	for i in range(0,dimension):
		summation = summation + (data[i] - reference[i])**2
	
	distance = math.sqrt(summation)
	return distance


#takes all the points and computes each distance to put into file, returns a list
#tested and works correctly
def total_values(list_data):

	totals = []
	for i in range(0, len(list_data)):
		origin = []
		for j in range (0, len(list_data[i])): ##generating origin point
			origin.append(0)
		x = distance(list_data[i], origin)
		totals.append(x)
	return totals

def write_to_file(file, points, distances):
	lookup = {}
	with open(file, 'w') as f:
		new_points = [tuple(x) for x in points] ##convert points list to tuple
		for x,y in zip(new_points, distances):
			lookup[x] = y

			#line = new_points[x] +":"+" "+distances[y]
			#f.write(line)
		new = sorted(lookup.items(), key = lambda x:x[1])
		#print(new)
		for x in new:
			line = '{}: {} \n'.format(x[0], x[1])
			#print(line)
			f.write(line)
	return f		


points = input("Enter a point: ")
collection = []

while len(points) > 0:
	collection.append(points)
	points = input("Enter a point: ")

filepath = input("Enter a destination file path: ")
clean_data = convert_to_list(collection)
distances = total_values(clean_data)
output = write_to_file(filepath,clean_data,distances)


