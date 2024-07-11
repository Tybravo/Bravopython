total = 0
score = int(input("Enter Score: "))
counter = 0

while score != -1:
	counter += 1
	total += score
	score = int(input("Enter Score: "))

average = total / counter
print(average)







