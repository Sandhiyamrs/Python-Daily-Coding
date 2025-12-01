import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url).json()
print(f"{response['setup']} ... {response['punchline']}")
