from file1_duplicate_file_finder import find_duplicates

duplicates = find_duplicates("downloads/")

if duplicates:
    print("Duplicate files found:")
    for original, copies in duplicates.items():
        print(f"{original} → {copies}")
else:
    print("No duplicate files detected.")
