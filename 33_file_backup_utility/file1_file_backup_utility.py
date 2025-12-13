import shutil
import os
from datetime import datetime

def backup_file(file_path, backup_dir="backups"):
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

    os.makedirs(backup_path)
    shutil.copy(file_path, backup_path)

    print("Backup created at:", backup_path)

# Example
# backup_file("sample.txt")
