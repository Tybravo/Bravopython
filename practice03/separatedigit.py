#Question 3.9

#12345


entrynum = int(input("Enter five digit number to separate them: "))

entrynum_tostr = str(entrynum)
isentrynum = len(entrynum_tostr)

alldigits = []

while isentrynum != 5:
	if isentrynum != 5:
		print("The number must be five digit")
		entrynum = int(input("Enter five digit number to separate them: "))

		entrynum_tostr = str(entrynum)
		isentrynum = len(entrynum_tostr)

	if isentrynum == 5:


		for count in range(5):
			eachdigit = entrynum // 10**(4 - count) % 10
			
			alldigits.append(eachdigit)

		for eachdigit in alldigits:
			print(eachdigit, end=' \n')

