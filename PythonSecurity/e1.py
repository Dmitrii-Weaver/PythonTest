# Write a Python program that defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string.

import hashlib


def hash_password(password):
    # encoding the password as bytes
    password_bytes = password.encode('utf-8')

    # using SHA-256 hash function to create a hash object
    hash_object = hashlib.sha256(password_bytes)

    # getting the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()

    return password_hash


password = input("Input your password: ")
hashed_password = hash_password(password)
print(f"Your hashed password is: {hashed_password}")
