from solution import fetch_weather

city = "Bangalore"
data = fetch_weather(city)

print(f"Weather Report for {city}")
print(data)
