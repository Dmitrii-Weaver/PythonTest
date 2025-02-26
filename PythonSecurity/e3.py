# Write a Python program to check if a password meets the following criteria:
# At least 8 characters long and
# Contains at least one uppercase letter, one lowercase letter, one digit, and one special character (!, @, #, $, %, or &)
# If the password meets the criteria, print a message that says "Valid Password." If it doesn't meet the criteria, print a message that says "Password does not meet requirements."

import re


def validate_password(password):
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

password = input("Input your password: ")
is_valid = validate_password(password)

if is_valid:
    print("Valid Password.")
else:
    print("Password does not meet requirements.")
