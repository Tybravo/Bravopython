#Quuestion 3.1


isnumber = int(input("Collect student score or enter 1 to stop iput: "))

totalpassed = 0
currentfailed = 0
totalfailed = 0
totalpassed = 0
counter = 0
firstcounter = 0
secondcounter = 0

while isnumber != 1:
		if isnumber >= 40 and isnumber <= 100:
			firstcounter = 1
			print("The student passed with a score of ", isnumber)
			print("Current number of student passed is ", firstcounter)

			totalpassed = totalpassed + firstcounter
			
			print("Total number of student passed is ", totalpassed)
			isnumber = int(input("Collect student score or enter 1 to stop iput: "))
			

		elif isnumber > 0 and isnumber < 40:
			secondcounter = 1
			print("The student failed with a score of ", isnumber)
			print("Current number of student failed is ", secondcounter)

			totalfailed = totalfailed + secondcounter
			
			print("Total number of student failed is ", totalfailed)
			isnumber = int(input("Collect student score or enter 1 to stop iput: "))

		elif isnumber > 100:
			print("You have entered a score out of range")
			isnumber = int(input("Collect student score or enter 1 to stop iput: "))

		else:
			print("Application Ended")
			break;



