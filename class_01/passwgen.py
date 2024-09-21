import random
import string

global random_number, random_upper_letter, random_lower_letter

def passw_gen():
    collect_number = []
    collect_lower_letter = []
    collect_upper_letter = []
    collect_symbol = []
    characters = "@#$%&*()_"

    for data in range (5):
        random_number = random.choice(string.digits)
        collect_number.append(random_number)
    for _ in range (5):
        random_lower_letter = random.choice(string.ascii_lowercase)
        collect_lower_letter.append(random_lower_letter)
    for _ in range (5):
        random_upper_letter = random.choice(string.ascii_uppercase)
        collect_upper_letter.append(random_upper_letter)
    for _ in range (3):
        random_special = random.choice(characters)
        collect_symbol.append(random_special)

    password_generator = collect_number + collect_lower_letter + collect_upper_letter + collect_symbol
    random.shuffle(password_generator)
    return (f" {''.join(password_generator)} {len(collect_number)} {len(collect_lower_letter)} {len(collect_upper_letter)} {len(collect_symbol)} {len(password_generator)}")

print(passw_gen())


