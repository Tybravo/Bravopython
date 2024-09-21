import random
import string
import re


def passw_gen():
    global random_number, random_upper_letter, random_lower_letter

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

    password_generator = "".join(password_generator)
    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+[@-A-Za-z0-9.-]', password_generator):
        random.shuffle(password_generator)

    return (f" {''.join(password_generator)} {len(collect_number)} {len(collect_lower_letter)} {len(collect_upper_letter)} {len(collect_symbol)} {len(password_generator)}")

print(passw_gen())



