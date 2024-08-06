#Question 4

print("""The mystery function sums up the 
sqaure of the numbers in the list""")

def mystery(x):
	y = 0
	for value in x:
		y += value ** 2
	return y

print(mystery([1, 2, 3, 4, 5]))





