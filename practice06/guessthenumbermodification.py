#Question 4.11

#user input first guess
#check if the guess is not correct (if the guess is  higher than 1000 or lower than 1
#diplay too high or too low and try again to input anothe guess number
# computer to set a random number
#prompt the user for the next guess
#if the user enters the correct guess, congratulate the user.


import random
isnumber = int(input("Guess my number between 1 and 15: "))

rightrandom = random.randint(1, 15)
counter = 1;
while isnumber  != -1:
	counter += 1;
	#if counter <= 10 and :
		#print("Either you know the secret or you got lucky!")

	if isnumber < 1 or isnumber > 15:
		print("The number is too high or low, try again")
		isnumber = int(input("Guess my number between 1 and 15 or -1 to quit: "))

	elif isnumber == rightrandom and counter <= 10:
		print("Congratulation!!")
		print("Either you know the secret or you got lucky!")
		isnumber = int(input("Guess my number between 1 and 15 or -1 to quit: "))
	
	elif isnumber != rightrandom: and counter > 10
		print("Wrong guess!!")
		print("You should be able to do better!")
		isnumber = int(input("Guess my number between 1 and 15 or -1 to quit: "))


	if isnumber == -1:
		print("Thank you for playing the guess game!")
		
