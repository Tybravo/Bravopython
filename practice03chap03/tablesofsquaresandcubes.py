#Question 3.7


print('number\tsquare\tcube\t')

for number in range(6):
	for square in range(1):
		for cube in range(1):
			square = number ** 2
			cube = number ** 3
			print(f' {number:>4} {square:>6} {cube:>7} ')






