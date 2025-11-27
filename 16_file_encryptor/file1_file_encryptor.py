from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(path):
    key = load_key()
    fernet = Fernet(key)

    with open(path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(path, "wb") as f:
        f.write(encrypted)

def decrypt_file(path):
    key = load_key()
    fernet = Fernet(key)

    with open(path, "rb") as f:
        data = f.read()

    decrypted = fernet.decrypt(data)

    with open(path, "wb") as f:
        f.write(decrypted)
