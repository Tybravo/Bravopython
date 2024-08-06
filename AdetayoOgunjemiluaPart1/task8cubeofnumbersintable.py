
a = "a"
b = "b"
c = "a^c"

print(f" {a:>3}{b:>4}{c:>8} ")

for a in range(1, 6):
	for b in range(1):
		for c in range(1):
			b = a + 1
			c = a**b
			print(f" {a:>3} {b:>3} {c:>6} ")
	
