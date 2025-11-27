import requests

API_KEY = "your_api_key_here"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    if res.get("main"):
        print("Temperature:", res["main"]["temp"])
        print("Weather:", res["weather"][0]["description"])
    else:
        print("City not found!")
