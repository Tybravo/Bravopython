import re

def validate_email(email):

    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+[@-A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}', email):
        return True
    else:
        return False

print(validate_email("Tybravo@home.com"))
