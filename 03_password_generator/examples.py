from solution import convert_currency

if __name__ == "__main__":
    amount = 100
    result = convert_currency(amount, "USD", "INR")
    print(f"{amount} USD = {result} INR")
