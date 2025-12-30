from file1_file_backup_utility import backup_files

backup_files(
    source_dir="project_data/",
    backup_dir="daily_backup/",
    compress=False
)

print("Daily backup finished.")
