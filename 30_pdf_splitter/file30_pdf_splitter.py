from PyPDF2 import PdfReader, PdfWriter

pdf_file = input("Enter PDF file path: ")
reader = PdfReader(pdf_file)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as f:
        writer.write(f)
    print(f"Saved page_{i+1}.pdf")
