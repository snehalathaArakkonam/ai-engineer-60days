"""
Project Title: Weather API App (OpenWeatherMap)

Project Description:
Fetch current weather for a user-provided city using the OpenWeatherMap API.
Displays temperature, humidity and weather description.

Concepts Used:
- HTTP requests using `requests`
- JSON parsing
- Environment variables for API key
- Error handling

API Integration Guide:
1. Sign up at https://openweathermap.org/ and get an API key (free tier available).
2. You can set the API key as environment variable `OPENWEATHER_API_KEY` or paste it
   when prompted by the program.
3. The program uses current weather endpoint.

Run:
python weather_api_app.py
"""

import os
import requests


API_URL = 'https://api.openweathermap.org/data/2.5/weather'


def get_api_key():
    """Retrieve API key either from environment or by asking the user."""
    key = os.getenv('OPENWEATHER_API_KEY')
    if key:
        return key
    return input('Enter OpenWeatherMap API key (or set OPENWEATHER_API_KEY env variable): ').strip()


def fetch_weather(city: str, api_key: str):
    """Fetch weather data for a city. Returns JSON dict or raises on error."""
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    resp = requests.get(API_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def display_weather(data: dict):
    """Extract and print Temperature, Humidity and Description from response."""
    main = data.get('main', {})
    wind = data.get('wind', {})
    weather_list = data.get('weather', [])
    description = weather_list[0].get('description') if weather_list else 'N/A'

    temp = main.get('temp')
    humidity = main.get('humidity')

    print(f"\nWeather for {data.get('name', 'Unknown')}")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")


def main():
    print('Weather API App')
    try:
        api_key = get_api_key()
        if not api_key:
            print('API key is required. Exiting.')
            return
        city = input('Enter city name: ').strip()
        if not city:
            print('City name required. Exiting.')
            return

        data = fetch_weather(city, api_key)
        display_weather(data)

    except requests.HTTPError as he:
        print(f'HTTP error: {he}')
    except requests.RequestException as re:
        print(f'Network error: {re}')
    except Exception as exc:
        print(f'Error: {exc}')


if __name__ == '__main__':
    main()
