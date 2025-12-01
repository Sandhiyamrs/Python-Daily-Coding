# file11_weather_app.py
import requests

def get_weather(city):
    API_KEY = "YOUR_API_KEY"  # e.g., OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {city}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found!")

city = input("Enter city name: ")
get_weather(city)
