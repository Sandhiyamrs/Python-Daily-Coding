import re

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1

    levels = ["Weak", "Moderate", "Strong", "Very Strong"]
    print("Password Strength:", levels[min(score, 3)])

# Example
check_strength("Hello@123")
