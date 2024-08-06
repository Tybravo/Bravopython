# define the name of the function to receive a parameter for integers
# prepare a container to save the integers
# split the integers by finding the modulo of the integers by 10 and adding it to the multiplication of expected result by 10
# get the remainder of the integer at each repitition of modulo division
# store the result in the prepared container
# divide the integer by 10 to get the whole number at each repitition untill the integer becomes 0



#reversenum = 0
#isnumber = int(input("Enter a number: "))
def reversenumber(isnumber):
	isnumber = str(isnumber)
	revnum =""
for character in isnumber:
		revnum = character + revnum
		revnumber = int(revnum)
		#return f" The reversed number is {revnumber} "
		return revnumber


#print(f" The reversed number is {revnumber} ")

print(reversenumber(5678))


