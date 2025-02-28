# Write a Python program that reads a file containing a list of passwords, one per line.
# It checks each password to see if it meets certain requirements (e.g. at least 8 characters,
# contains both uppercase and lowercase letters, and at least one number and one special character).
# Passwords that satisfy the requirements should be printed by the program.

import re
def check_password(password):
    length_regex = re.compile(r'^.{8,}$')
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')
    special_regex = re.compile(r'[\W_]')
    
    length_check = length_regex.search(password)
    uppercase_check = uppercase_regex.search(password)
    lowercase_check = lowercase_regex.search(password)
    digit_check = digit_regex.search(password)
    special_check = special_regex.search(password)
    
    if length_check and uppercase_check and lowercase_check and digit_check and special_check:
        return True
    else:
        return False

with open('passwords.txt') as f:
    for password in f:
        password = password.strip()  
        if check_password(password):
            print("Valid Password: "+password)
        else:
            print("Invalid Password: "+password)
