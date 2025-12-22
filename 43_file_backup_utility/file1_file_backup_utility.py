import shutil
import time

def backup_file(file_path):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_name = f"{file_path}_{timestamp}.bak"
    shutil.copy(file_path, backup_name)
    print("Backup created:", backup_name)

# Example
# backup_file("data.txt")
