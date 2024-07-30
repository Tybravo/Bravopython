#move through the numbers between 1000 and 3000
#divide each of the numbers by 2 
#if the result gotten in step three is equals to zero, store  is a container
#print to display the container


for number in range(1000, 3002, 2):
	firstdigit = number // 1000 % 10
	seconddigit = number // 100 % 10
	thirddigit = number //10 % 10
	fourthdigit = number % 10

	if firstdigit % 2 == 0 and seconddigit % 2 == 0 and thirddigit % 2 == 0 and fourthdigit % 2 == 0:
		print(number, end =",")