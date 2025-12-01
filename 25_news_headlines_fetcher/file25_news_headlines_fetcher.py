import requests

API_KEY = "YOUR_NEWSAPI_KEY"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url).json()
for i, article in enumerate(response['articles'][:10], 1):
    print(f"{i}. {article['title']}")
