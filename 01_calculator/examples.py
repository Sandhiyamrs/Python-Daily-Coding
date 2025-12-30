from solution import find_duplicates

if __name__ == "__main__":
    folder_path = "./test_data"
    duplicates = find_duplicates(folder_path)

    if duplicates:
        print("Duplicate files found:")
        for file in duplicates:
            print(file)
    else:
        print("No duplicate files found.")
