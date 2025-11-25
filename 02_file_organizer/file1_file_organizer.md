# File Organizer - file1

import os
import shutil

def organize(folder):
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)
        ext = ext[1:]

        if ext:
            path = os.path.join(folder, ext)

            if not os.path.exists(path):
                os.makedirs(path)

            shutil.move(os.path.join(folder, filename), os.path.join(path, filename))

folder_path = input("Enter folder path: ")
organize(folder_path)
print("Files organized successfully!")
