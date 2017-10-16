import math

def quadratic(A,B,C):
	x_1 = (-B + math.sqrt((B**2 - 4*A*C)))/ (2*A)
	x_2 = (-B - math.sqrt((B**2 - 4*A*C)))/ (2*A)

	return x_1, x_2


	