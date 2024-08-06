#Question 4.9

def convert_temp(celsius, fahrenheit):
	fahrenheit = 0
	fahrenheit = (9 / 5) * celsius + 32
		

def print_temp_table():
	print(f" {"Celsius":>10} {"Fahrenheit":>15}")
	print("_" * 25)

	for celsius in range(101):
		fahrenheit = 0
		fahrenheit = (9 / 5) * celsius + 32
		#fahrenheit = f" {celsius:>10} {fahrenheit:>15} "
		print(f" {celsius:>10} {fahrenheit:>15} ")
		
		#return fahrenheit

print_temp_table()

print(convert_temp(fahrenheit))


