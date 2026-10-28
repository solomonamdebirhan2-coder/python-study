
import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score <= 3:
        return "Medium Password"
    elif score == 4:
        return "Strong Password"
    else:
        return "Very Strong Password"


password = input("Enter your password: ")

result = check_password_strength(password)

print("Password Strength:", result)
