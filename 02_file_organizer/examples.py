from solution import save_password, get_password

if __name__ == "__main__":
    save_password("gmail", "mySecurePass123")
    print("Password stored successfully")

    pwd = get_password("gmail")
    print("Retrieved password:", pwd)
