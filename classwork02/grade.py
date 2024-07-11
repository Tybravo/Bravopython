gradescore = int(input("Enter Score to determine the grade: "))


if gradescore > 100:
	print("No grade for the score")
elif gradescore >= 75 and gradescore <=100:
	print("A")
elif gradescore >= 65 and gradescore <=74:
	print("B")
elif gradescore >= 50 and gradescore <=64:
	print("C")
elif gradescore >= 40 and gradescore <=49:
	print("D")
else:
 	print("F")








