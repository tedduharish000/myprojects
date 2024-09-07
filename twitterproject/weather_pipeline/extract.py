import requests
import pandas as pd
from datetime import datetime

# Your OpenWeatherMap API key
API_KEY = '778e19ff2c03dc773e8010c15638e9e7'
CITY = "London"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        # Extract relevant data
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'weather': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'timestamp': datetime.now()
        }
        return weather_info
    else:
        print(f"Error: {data['message']}")
        return None

