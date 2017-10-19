import random as rd


#counts how many points lie within a circle
def point_in_circle(points, sq_length):
	center = [0.5,0.5]
	diameter = sq_length
	radius = float(diameter)/2
	count = 0
	for point in points:
		distance = (point[0] - center[0])**2 + (point[1] - center[1])**2
		if distance <= radius**2:
			count = count + 1
	return count

##generating the random points
def generate_points(n):
	points = []
	for i in range(0,n):
		value = [rd.random(), rd.random()]
		points.append(value)
	return points


def calculate_pi(n):
	length_square = 1
	diameter = length_square
	values = generate_points(n)
	number_in = point_in_circle(values,length_square)
	total_points = n
	circle_area = (length_square**2) * (float(number_in)/total_points)
	pi = (4*circle_area)/ float((diameter**2))
	return pi

#points = [[0,2], [1,5], [0.5,0.6]]
#print(point_in_circle(points,length_square))

#print(generate_points(5))
#print(calculate_pi(100000))



