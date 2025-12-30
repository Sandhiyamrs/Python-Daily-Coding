import hashlib
import os
from pathlib import Path
from collections import defaultdict

def calculate_hash(filepath, algorithm='md5'):
    """Calculate hash of a file."""
    hash_func = hashlib.md5() if algorithm == 'md5' else hashlib.sha256()
    
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def find_duplicates(directory):
    """Find duplicate files in directory."""
    # Group files by size
    size_map = defaultdict(list)
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                file_size = os.path.getsize(filepath)
                size_map[file_size].append(filepath)
            except OSError:
                continue
    
    # Find duplicates among files with same size
    duplicates = defaultdict(list)
    
    for size, files in size_map.items():
        if len(files) < 2:
            continue
        
        hash_map = defaultdict(list)
        for filepath in files:
            try:
                file_hash = calculate_hash(filepath)
                hash_map[file_hash].append(filepath)
            except OSError:
                continue
        
        for file_hash, duplicate_files in hash_map.items():
            if len(duplicate_files) > 1:
                duplicates[file_hash] = duplicate_files
    
    return duplicates

def main():
    print("=== Duplicate File Finder ===\n")
    
    directory = input("Enter directory path to scan: ").strip()
    
    if not os.path.exists(directory):
        print("Error: Directory does not exist!")
        return
    
    print(f"\nScanning directory: {directory}")
    print("This may take a while for large directories...\n")
    
    duplicates = find_duplicates(directory)
    
    if not duplicates:
        print("No duplicate files found!")
        return
    
    print(f"Found {len(duplicates)} sets of duplicate files:\n")
    
    total_duplicates = 0
    wasted_space = 0
    
    for idx, (file_hash, files) in enumerate(duplicates.items(), 1):
        print(f"Duplicate Set {idx}:")
        file_size = os.path.getsize(files[0])
        print(f"  Size: {file_size / 1024:.2f} KB")
        print(f"  Hash: {file_hash}")
        
        for file in files:
            print(f"    - {file}")
        
        total_duplicates += len(files) - 1
        wasted_space += file_size * (len(files) - 1)
        print()
    
    print(f"Total duplicate files: {total_duplicates}")
    print(f"Wasted space: {wasted_space / (1024*1024):.2f} MB")
    
    # Option to delete duplicates
    delete = input("\nDo you want to delete duplicates? (keep first file) (y/n): ").lower()
    
    if delete == 'y':
        deleted_count = 0
        for files in duplicates.values():
            for file in files[1:]:  # Keep first file, delete rest
                try:
                    os.remove(file)
                    print(f"Deleted: {file}")
                    deleted_count += 1
                except OSError as e:
                    print(f"Error deleting {file}: {e}")
        
        print(f"\nDeleted {deleted_count} duplicate files!")

if __name__ == "__main__":
    main()
