age = int(input("Enter your age: "))

if age >= 18 and age <= 45:
	print('You are eligible to make your own decisions')
	print("Hello")
	print('Techblazers')
elif age >= 13 and age <= 19:
	print("You are a teenager")
	print("Hello")
elif age >= 0 and age <= 13:
	print("You are still a child")

else:
	print('You are old')