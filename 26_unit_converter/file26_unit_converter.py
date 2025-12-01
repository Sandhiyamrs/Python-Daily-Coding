def convert_length(value, from_unit, to_unit):
    conversions = {"m": 1, "cm": 0.01, "km": 1000}
    return value * conversions[from_unit] / conversions[to_unit]

value = float(input("Enter value: "))
from_unit = input("From unit (m/cm/km): ").lower()
to_unit = input("To unit (m/cm/km): ").lower()
print(f"{value} {from_unit} = {convert_length(value, from_unit, to_unit)} {to_unit}")
