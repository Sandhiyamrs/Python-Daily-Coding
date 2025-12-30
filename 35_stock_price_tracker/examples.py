from file1_stock_price_tracker import get_stock_price

symbols = ["AAPL", "GOOGL", "TSLA"]

for stock in symbols:
    print(stock, "Price:", get_stock_price(stock))
