#Question 3.11


milespergallon = 0
combinedmilespergallon = 0

milesdriven = int(input("Enter miles driven or  -1 to stop: "))
gallonused = int(input("Enter gallon used: "))
	
	

while milesdriven != -1:
	milespergallon = milesdriven / gallonused
	print("The miles per gallon for this tank is ", milespergallon )
	
	combinedmilespergallon = combinedmilespergallon + milespergallon
	
	milesdriven = int(input("Enter miles driven or  -1 to stop: "))

	if milesdriven == -1:
		print("Combined miles per gallon used is ", combinedmilespergallon)
	else:
		gallonused = int(input("Enter gallon used: "))
	
	






