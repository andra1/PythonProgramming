
def number_manipulation_maker(string, y):
	if string == 'add':
		def add(x):
			return x + y
		return add

	elif string == 'multiply':
		def multiply(x):
			return x*y
		return multiply

	elif string == 'divide':
		def divide(x):
			x = float(x)
			return x/y
		return divide

	elif string  == 'subtract':
		def subtract(x):
			return x - y
		return subtract

	elif string == 'exponent':
		def exponent(x):
			return x**y
		return exponent
	else:
		pass


#operation = number_manipulation_maker('exponent', 3)
#print(operation(11))