import hashlib

def calculate_checksum(file_path, method="sha256"):
    hash_func = hashlib.sha256() if method == "sha256" else hashlib.md5()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)

    return hash_func.hexdigest()

file_path = input("Enter file path: ")
method = input("Enter method (sha256/md5): ").lower()

checksum = calculate_checksum(file_path, method)
print(f"{method.upper()} Checksum:", checksum)

verify = input("Do you want to verify a checksum? (yes/no): ")

if verify.lower() == "yes":
    user_checksum = input("Enter checksum to compare: ")
    if user_checksum == checksum:
        print("✔ File is authentic!")
    else:
        print("✘ Checksum mismatch!")
