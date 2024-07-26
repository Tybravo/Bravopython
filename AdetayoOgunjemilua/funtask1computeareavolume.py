def computeareavolume(radius, length):
	pie = 3.142		
	isarea = pie * (radius ** 2)
	isvolume = isarea * length

	return f"{isarea} {isvolume} "

print(computeareavolume(5, 12))

