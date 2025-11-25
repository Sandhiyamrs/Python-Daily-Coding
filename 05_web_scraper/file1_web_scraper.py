# Web Scraper - file1

import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Page Title:", soup.title.string)
