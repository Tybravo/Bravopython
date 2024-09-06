
#class biggest_odd:
"""
def biggest_odd(numbers):

    largest_num = ""

    for index in numbers:
        if int(index) > int(largest_num) and int(index) % 2 != 0:
            largest_num = int(index)

            return largest_num
"""


def biggest_odd(numbers):
	maximum = 0
	for index in numbers:
		if int(index) > maximum and int(index) % 2 != 0:
			maximum = int(index)

	return maximum
