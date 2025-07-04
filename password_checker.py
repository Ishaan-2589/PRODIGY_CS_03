import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    print("Password Strength:", end=" ")
    if strength <= 2:
        print("Weak")
    elif strength == 3 or strength == 4:
        print("Moderate")
    else:
        print("Strong")

# Input from user
password = input("Enter a password to check: ")
check_password_strength(password)