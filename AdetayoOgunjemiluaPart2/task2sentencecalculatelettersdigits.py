# prompt the user to accept a sentence
# read the sentence from the user
# count the number of letter in the sentence
# count the number of digits in the sentence
# save the counted letters in a container
# save the counted digits in a container.
# print to display the counted letter and digits

isSentence = input("Enter a sentence to get numbers of letters and digits: ")

getDigits = ""
getLetters = ""

for char in isSentence:
	if char.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
		getLetters += char
	if char.lower() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
		getDigits += char

print(f"The number of LETTERS is {len(getLetters)} \nThe number of DIGITS is {len(getDigits)} ")


