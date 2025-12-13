import re

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2 or score == 3:
        return "Medium"
    else:
        return "Strong"

# Example
pwd = "Hello@123"
print("Strength:", check_strength(pwd))
