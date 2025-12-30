from file1_file_backup_utility import backup_files

backup_files(
    source_dir="important_files/",
    backup_dir="backup/",
    compress=True
)

print("Backup completed successfully")
