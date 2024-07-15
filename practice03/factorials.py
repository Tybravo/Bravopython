#Question 3.13


collectnum = int(input("Enter a number to get its's factorial: "))

factorial = 1
collectnum = collectnum + 1

for count in range(1, collectnum):
	factorial = factorial * count
	#print(factorial)
else:
	print(factorial)

