# Duplicate File Finder

## Description
A utility that scans directories to find and identify duplicate files based on their content (using hash comparison).

## Features
- Recursive directory scanning
- MD5/SHA256 hash comparison
- Size-based pre-filtering
- Delete or move duplicates option
- Summary report generation

## Requirements
```
hashlib (built-in)
os (built-in)
pathlib (built-in)
```

## Usage
```python
python file1_duplicate_file_finder.py
```

## How It Works
1. Scans specified directory recursively
2. Groups files by size
3. Computes hash for files with same size
4. Identifies duplicates based on matching hashes
5. Provides options to delete or move duplicates
