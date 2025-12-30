from solution import generate_checksum, verify_checksum

checksum = generate_checksum("important.zip")
print("Checksum:", checksum)

print("Verification:", verify_checksum("important.zip", checksum))
