# CSV Reader - file1

import csv

file = input("Enter CSV file path: ")

with open(file, newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
