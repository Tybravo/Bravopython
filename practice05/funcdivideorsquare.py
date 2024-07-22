import math
def divide_or_square(isnumber):

	if isnumber % 5 == 0:
		squareroot = math.sqrt(isnumber)
		return f" {squareroot} "
	elif isnumber % 5 > 0:
		remainder = isnumber % 5
		return f" {remainder} "

print(divide_or_square(10))
