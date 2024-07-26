#promt the user to enter number of pounds
#read the number of pounds from the user
#declare  a kilogram per pound
#multiply the gotten pound from user by the kilogram per pound
#identify your result as the new gotten kilogram
#print to display in kilogram

collectpound = int(input("Enter the number of pound to get kilogram(s): "))

onepound_tokilogram =  0.454
getkilogram = onepound_tokilogram * collectpound

print("Pound in kilogram is ", getkilogram, "kilogram")


