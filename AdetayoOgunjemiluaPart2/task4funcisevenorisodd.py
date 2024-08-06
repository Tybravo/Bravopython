# prompt user to collect an integer number
# divide the collected number by 2
# if result from step two is equals to zero
# return the integer as even number
# else if result from step two is not equal to zero
# return the integer as odd number

#isNumber = input(int("Enter number to check if it is even or odd"))
def collect_integer(isNumber):

	if isNumber % 2 == 0:
		return f" {"It is an even number"} "
	else:
		return f" {"It is an odd number"} "

print(collect_integer(14))


