
def consonant_and_vowel(isword):
#isword = input("Enter word to get number of vowels and consonants: ")
	vowel = ""
	consonant =""

	for character in isword:
		if character.lower() in ['a', 'e', 'i', 'o', 'u']:
			vowel += character
		else:
			consonant += character

#print(f"The number of vowel is {len(set(vowel))} \n The number of consonant is {len(set(consonant))} ")

	return f"The number of vowel is {len(set(vowel))} \n The number of consonant is {len(set(consonant))} "

print(consonant_and_vowel('Bola'))
print(consonant_and_vowel('Adebisi'))







