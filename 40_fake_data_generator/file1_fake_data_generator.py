import random

first_names = ["John", "Jane", "Alex", "Emily"]
last_names = ["Doe", "Smith", "Brown", "Taylor"]

def generate_fake_user():
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first.lower()}.{last.lower()}@example.com"

    return {
        "Name": f"{first} {last}",
        "Email": email
    }

# Example
print(generate_fake_user())
