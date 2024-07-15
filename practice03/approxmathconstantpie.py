#Question 3.14


approxconstantpie = 0

for atcount in range(3, 12, 2):
	approxconstantpie = 4 - (4/atcount + 4/(atcount + 2))
	
	print(approxconstantpie, atcount, sep='    ')

