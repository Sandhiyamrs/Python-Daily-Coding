def stock_tracker(buy_price, current_price):
    diff = current_price - buy_price
    if diff > 0:
        print(f"Profit: ₹{diff}")
    else:
        print(f"Loss: ₹{abs(diff)}")

# Example
stock_tracker(1200, 1350)
