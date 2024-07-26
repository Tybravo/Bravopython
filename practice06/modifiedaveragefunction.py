#Question 4.6


def isaverage(isnumber, *args):
	
	average = sum(args) / len(args)
	return average
	
print(isaverage(6, 2, 4, 8, 10))


