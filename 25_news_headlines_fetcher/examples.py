from solution import fetch_headlines

headlines = fetch_headlines(country="in")
for h in headlines[:5]:
    print("-", h)
