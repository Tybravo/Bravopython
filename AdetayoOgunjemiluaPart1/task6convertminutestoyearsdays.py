#prompt the user to enter number of minutes
#collect the user inputs
#multiply 60 by 24 to get number of minutes in a day
#divide the collected input by the gotten number of minutes in a day and by number of days in a year
#divide the collected input by the gotten number of minutes in a day and by modulo number of days in a year
#identity the number of years and days as the result
#print to display result

collectminutes =  int(input("Enter number of minutes :"))

minutes_in_aday = 60 * 24

exactyears= collectminutes /minutes_in_aday /365
dayremaining = (collectminutes /minutes_in_aday) % 365

exactyears = exactyears // 1
dayremaining = dayremaining // 1

print("Years is ", exactyears, "Days is",dayremaining )
	


