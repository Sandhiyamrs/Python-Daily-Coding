from file1_stock_price_tracker import get_stock_price

portfolio = {
    "AAPL": 10,
    "MSFT": 5,
    "TSLA": 2
}

total_value = 0

for stock, qty in portfolio.items():
    price = get_stock_price(stock)
    value = price * qty
    total_value += value
    print(f"{stock} → {qty} shares → ₹{value:.2f}")

print("Portfolio Value: ₹", total_value)
