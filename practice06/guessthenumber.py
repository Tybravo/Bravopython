#Question 4.10

#user input first guess
#check if the guess is not correct (if the guess is  higher than 1000 or lower than 1
#diplay too high or too low and try again to input anothe guess number
# computer to set a random number
#prompt the user for the next guess
#if the user enters the correct guess, congratulate the user.


import random
isnumber = int(input("Guess my number between 1 and 5: "))

rightrandom = random.randint(1, 5)
		
while isnumber  != -1:
	if isnumber < 1 or isnumber > 5:
		print("The number is too high or low, try again")
	
		isnumber = int(input("Guess my number between 1 and 5 or -1 to quit: "))

	elif isnumber == rightrandom:
		print("Congratulation!!")
		isnumber = int(input("Guess my number between 1 and 5 or -1 to quit: "))
	
	elif isnumber != rightrandom:
		print("Wrong guess!!")
		isnumber = int(input("Guess my number between 1 and 5 or -1 to quit: "))


	if isnumber == -1:
		print("Thank you for playing the guess game!")
		
