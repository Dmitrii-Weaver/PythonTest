# Write a Python program that generates a password using a random combination of words from a dictionary file.

import random


def generate_password():
    with open('dictionary.txt') as f:
        words = f.read().splitlines()

    password = random.sample(words, 4)

    password = '-'.join(password)

    return password

password = generate_password()
print(password)
