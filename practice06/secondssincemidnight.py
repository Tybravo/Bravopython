#Question 5

def seconds_since_midnight(hour, minute, second):
	hour_in_seconds = hour * 60 * 60
	minute_in_seconds = minute * 60 + second
	getseconds = hour_in_seconds + minute_in_seconds

	return f" {getseconds} "

print(seconds_since_midnight(13, 30, 45))

