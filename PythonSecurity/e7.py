# Write a Python program that creates a password strength meter.
# The program should prompt the user to enter a password and check its strength based on criteria such as length,
# complexity, and randomness. Afterwards, the program should provide suggestions for improving the password's strength.

import re


def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append(
            "Password should contain at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append(
            "Password should contain at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append(
            "Password should contain at least one numeric digit")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append(
            "Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")

    return score, suggestions


password = input("Input a password: ")
print(check_password_strength(password))
