from solution import is_valid_email

emails = [
    "user@gmail.com",
    "invalid-email",
    "test@domain.co"
]

for email in emails:
    print(email, "->", is_valid_email(email))
