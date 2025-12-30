from file1_password_strength_checker import check_strength

passwords = ["hello123", "Admin@123", "Strong#Pass99"]

for pwd in passwords:
    print(pwd, "→", check_strength(pwd))
