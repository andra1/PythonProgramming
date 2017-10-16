import math

def area(shape, **dimensions):
	if shape == 'circle':
		if 'radius' in dimensions:
			value = math.pi * dimensions['radius']**2
			return value
		elif 'diameter' in dimensions:
			value = math.pi * (float(dimensions['diameter'])/ 2)**2
			return value

	elif shape == 'triangle':
		if 'base' and 'height' in dimensions:
			value = float(dimensions['base']) * float(dimensions['height']) * 0.5
			return value

	elif shape == 'rectangle':
		if 'length' and 'width' in dimensions:
			value = float(dimensions['length']) * float(dimensions['width'])
			return value

	else:
		return None

#print (area('triangle', base=20, height=5))
#testing out new commits
