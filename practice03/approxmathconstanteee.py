#Question 3.15


approxconstante = 0
factorial = 1
addon = 0

for atcount in range(1, 11):  
	factorial = factorial * atcount
	addon = addon + 1/factorial
	constant_e = addon + 1

	print(atcount, constant_e, sep='    ')

