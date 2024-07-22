#prompt to read scores from student
#loop to read score fifteen times at each prompting
#prompt to read scores from student
#determine if student pass or fail  (aove 45 is pass mark)
#count number of student that pass



scorecollection = int(input("Enter 15 student score to get total failed and passed: "))

passmark = 45
increasefail = 0
increasepass = 0
count = 0

while count != 5:
	count = count + 1
	if scorecollection > passmark or scorecollection == passmark:
		increasepass = increasepass + 1
		print("Passed with the score ", scorecollection)
		print("Total passed is ", increasepass)
		scorecollection = int(input("Enter 15 student score to get total failed and passed: "))

	elif scorecollection < passmark:
		increasefail = increasefail + 1
		print("Failed with the score ", scorecollection)
		print("Total failed is ", increasefail)
		scorecollection = int(input("Enter 15 student score to get total failed and passed: "))

	if count == 5:
		print("Total passed is ", increasepass)
		print("Total failed is ", increasefail)
	#print()







	