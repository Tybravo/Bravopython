#Question 3
What is wrong with this code below

"""
def cube(x):
#Calculate the cube of x.
 x ** 3
print('The cube of 2 is', cube(2))
"""
#What is wrong with this code above is that the function is returning nothing as NONE



def cube(x):
	iscube  =  x ** 3
	return iscube

print('The cube of 2 is', cube(2))
