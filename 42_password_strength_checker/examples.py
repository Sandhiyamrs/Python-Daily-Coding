from file1_password_strength_checker import check_strength

users = {
    "admin": "admin123",
    "developer": "Dev@Secure99",
    "guest": "guest"
}

for user, pwd in users.items():
    print(f"{user} → {check_strength(pwd)}")
