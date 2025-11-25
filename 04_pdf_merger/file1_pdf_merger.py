# PDF Merger - file1

from PyPDF2 import PdfMerger

merger = PdfMerger()

num = int(input("How many PDFs to merge? "))

for i in range(num):
    pdf = input(f"Enter PDF {i+1} path: ")
    merger.append(pdf)

output = input("Output file name: ")
merger.write(output)
merger.close()

print("PDFs merged successfully!")
