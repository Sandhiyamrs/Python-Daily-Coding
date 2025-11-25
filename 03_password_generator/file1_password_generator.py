# Password Generator - file1

import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    return password

print("Generated Password:", generate_password())
