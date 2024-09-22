
import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)

print(random_number)


###########################################################################################################

import random

# Generate 5 random integers between 1 and 100
for _ in range(5):
    print(random.randint(1, 100))


#########################################################################################################


random_number = random.randrange(1, 10)  # Generates a number between 1 and 9 (inclusive of 1, but exclusive of 10)
print(random_number)


import random
import string

# Generate a random lowercase letter
random_lowercase_letter = random.choice(string.ascii_lowercase)
print(random_lowercase_letter)

# Generate a random uppercase letter
random_uppercase_letter = random.choice(string.ascii_uppercase)
print(random_uppercase_letter)

# Generate a random letter (uppercase or lowercase)
random_letter = random.choice(string.ascii_letters)
print(random_letter)

# Generate a random digit
random_digit = random.choice(string.digits)
print(random_digit)


#########################################################################################


import random

# Custom character set
characters = 'ABCDEF123456!@#'

# Generate a random character from the custom set
random_char = random.choice(characters)
print(random_char)



#############################################################################################


import random
import string

# Generate 5 random lowercase letters
random_letters = [random.choice(string.ascii_lowercase) for _ in range(5)]
print(''.join(random_letters))

# Generate 5 random characters from a custom set
characters = 'ABCDEF123456!@#'
random_custom_chars = [random.choice(characters) for _ in range(5)]
print(''.join(random_custom_chars))


#############################################################################################