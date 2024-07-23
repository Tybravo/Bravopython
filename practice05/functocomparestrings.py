
def equal_strings(wordone, wordtwo):


	for characters in wordone:
		for characters in wordtwo:
			if len(set(wordone)) == len(set(wordtwo)):
				return "true"
	else:
				return "false"


print(equal_strings('love', 'evols'))





