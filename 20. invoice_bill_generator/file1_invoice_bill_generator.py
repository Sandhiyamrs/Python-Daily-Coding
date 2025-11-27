invoice = []
tax_rate = 0.05

while True:
    name = input("Item name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price per item: "))

    invoice.append([name, qty, price, qty * price])

    more = input("Add more items? (yes/no): ")
    if more.lower() != "yes":
        break

print("\n--- Invoice Bill ---")
total = 0

for item in invoice:
    print(f"{item[0]} - Qty: {item[1]}, Price: {item[2]}, Total: {item[3]}")
    total += item[3]

tax = total * tax_rate
grand_total = total + tax

print("\nSubtotal:", total)
print("Tax (5%):", tax)
print("Grand Total:", grand_total)
