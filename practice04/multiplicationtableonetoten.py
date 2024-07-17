
isnumber = int(input("Enter a numer for multiplication of 1 to 10: "))

times = "x"
equals = "="

for count in range(1, 11):
	getresult = isnumber * count

	#print(getresult)

	print(isnumber, times, count, equals, getresult, sep='  ')


