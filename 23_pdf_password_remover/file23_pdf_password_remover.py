from PyPDF2 import PdfReader, PdfWriter

pdf_file = input("Enter PDF file path: ")
password = input("Enter PDF password: ")
output_file = "unlocked_" + pdf_file

reader = PdfReader(pdf_file)
if reader.is_encrypted:
    reader.decrypt(password)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"PDF unlocked and saved as {output_file}")
else:
    print("PDF is not encrypted.")
