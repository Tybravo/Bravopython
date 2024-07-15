#Question 3.12

firstdigit = 0
seconddigit = 0
thirddigit = 0
fourthdigit = 0
fifthdigit = 0


entrydigit = int(input("Enter five dgit for palindrome check: "))

entrydigit_tostr = str(entrydigit)
isentrydigit = len(entrydigit_tostr)


while isentrydigit != 5:
	if isentrydigit != 5:
		print("The number must be five digit")
		entrydigit = int(input("Enter five dgit for palindrome check: "))


		entrydigit_tostr = str(entrydigit)
		isentrydigit = len(entrydigit_tostr)

	if isentrydigit == 5:
		firstdigit = entrydigit // 10000 % 10
		seconddigit = entrydigit // 1000 % 10
		thirddigit = entrydigit // 100 % 10
		fourthdigit = entrydigit //10 % 10
		fifthdigit = entrydigit % 10

	if firstdigit == fifthdigit and seconddigit == fourthdigit and isentrydigit == 5:
		print("Yes! The digits you entered is a Palindrome")
	
	elif firstdigit != fifthdigit and seconddigit != fourthdigit and isentrydigit == 5:
		print("Noway! The digits you entered is not Palindrome")
	
	print(firstdigit, seconddigit, thirddigit, fourthdigit, fifthdigit, end='   ')