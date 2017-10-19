import sys

def fibonacci(n):
	if n == 0:
		#print(1)
		return 1
	elif n == 1:
		#print(1)
		return 1
	else:
		#print(fibonacci(n-1) + fibonacci(n-2))
		return fibonacci(n-1) + fibonacci(n-2)

x = int(sys.argv[1])
[print(fibonacci(y)) for y in range(0,x+1)]