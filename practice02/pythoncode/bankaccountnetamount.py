entry = int(input("Enter 1 to deposit , 2 to widthraw or -1 to quit: "))
count = 0
totalbalance = 0
		
while entry != -1:
	if entry ==1:
		deposit = int(input("Enter amount to deposit or -1 to quit: "))
		totalbalance += deposit
		print("total balance is ",totalbalance)
		entry = int(input("Enter 1 to deposit , 2 to widthraw or -1 to quit: "))
		
	elif entry ==2:
		widthraw = int(input("Enter amount to widthraw or -1 to quit: "))
		totalbalance -= widthraw
		print("total balance is ",totalbalance)
		entry = int(input("Enter 1 to deposit , 2 to widthraw or -1 to quit: "))
	
	else:
		print("Invalid input")
		entry = int(input("Enter 1 to deposit , 2 to widthraw or -1 to quit: "))












