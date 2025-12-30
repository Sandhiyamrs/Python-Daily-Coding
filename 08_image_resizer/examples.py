from solution import encrypt_file, decrypt_file

encrypt_file("sample.txt", "secret.key")
print("File encrypted")

decrypt_file("sample.txt.enc", "secret.key")
print("File decrypted")
