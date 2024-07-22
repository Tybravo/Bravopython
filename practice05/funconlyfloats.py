
def only_floats(numberone, numbertwo):
	isnumberone = isinstance(numberone,float)
	isnumbertwo = isinstance(numbertwo, float)

	if isnumberone and isnumbertwo:
		return 2

	if isnumberone or isnumbertwo:
		return 1

	else:
		return 0


print(only_floats(121, 23))


