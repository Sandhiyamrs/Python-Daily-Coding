import os

def search_files(directory, keyword):
    for root, _, files in os.walk(directory):
        for file in files:
            if keyword.lower() in file.lower():
                print("Found:", os.path.join(root, file))

# Example
# search_files(".", "report")
