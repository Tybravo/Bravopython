
def do_stuff(number, list_of_numbers):
	for numba in list_of_numbers:
		number += numba
	return number

print(do_stuff(10, [1,2,3,4,5]))
print(do_stuff(list_of_numbers = [1,2,3,4,5], number = 10))

#list_of_numbers = [1,2,3,4,5] refers to the positional argument
#number = 10 refers to the keyword argumaent



