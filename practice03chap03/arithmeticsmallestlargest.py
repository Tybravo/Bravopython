#Question 3.8


count = 0
sum = 0
product = 1
average = 0

firstnum = 0
secondnum = 0
thirdnum = 0
fourthnum = 0
largestnumber = 0
smallestnumber = 0

for number in range(1, 5):
	count += 1
	number = int(input("Enter number "+ str(count) +": "))
	
	sum = sum + number
	product = product * number
	average = sum / count

	

	if count == 1:
		firstnum = number
	if count == 2:
		secondnum = number
	if count == 3:
		thirdnum = number
	if count == 4:
		fourthnum = number

	if firstnum > secondnum and firstnum > thirdnum and firstnum > fourthnum:
		largestnumber = firstnum

	elif secondnum > firstnum and secondnum > thirdnum and secondnum > fourthnum:
		largestnumber = secondnum

	elif thirdnum > firstnum and thirdnum > secondnum and thirdnum > fourthnum:
		largestnumber = thirdnum	

	elif fourthnum > firstnum and fourthnum > secondnum and fourthnum > thirdnum:
		largestnumber = fourthnum	


	if firstnum < secondnum and firstnum < thirdnum and firstnum < fourthnum:
		smallestnumber = firstnum

	elif secondnum < firstnum and secondnum < thirdnum and secondnum < fourthnum:
		smallestnumber = secondnum

	elif thirdnum < firstnum and thirdnum < secondnum and thirdnum < fourthnum:
		smallestnumber = thirdnum	

	elif fourthnum < firstnum and fourthnum < secondnum and fourthnum < thirdnum:
		smallestnumber = fourthnum	
	

	if count == 4:
		print("Total sum is ", +sum)
		print("Product is ", +product)
		print("Average is ", +average)
		print("Largest number is ", +largestnumber)
		print("Smallest number is ", smallestnumber)










