from solution import generate_invoice

items = [
    ("Laptop", 1, 55000),
    ("Mouse", 2, 500)
]

generate_invoice("invoice_101.pdf", items)
print("Invoice generated successfully")
