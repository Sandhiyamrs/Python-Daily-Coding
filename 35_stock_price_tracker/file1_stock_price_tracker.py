def stock_tracker(price_yesterday, price_today):
    change = ((price_today - price_yesterday) / price_yesterday) * 100
    print(f"Price Today: ₹{price_today}")
    print(f"Change: {change:.2f}%")

# Example
stock_tracker(115, 120)
