"""
Project Title: Weather Dashboard (Terminal)

Project Description:
Terminal dashboard to search a city and display temperature, humidity, wind
speed and weather condition using OpenWeatherMap API. Provides a compact
dashboard-style display in the terminal.

Concepts Used:
- API requests, JSON parsing, formatted terminal output

Run:
python weather_dashboard.py
"""

import os
import requests


API_URL = 'https://api.openweathermap.org/data/2.5/weather'


def get_api_key():
    key = os.getenv('OPENWEATHER_API_KEY')
    if key:
        return key
    return input('Enter OpenWeatherMap API key: ').strip()


def fetch_weather(city, api_key):
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    resp = requests.get(API_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def dashboard_line(label, value, width=20):
    return f"{label:<{width}}: {value}"


def display_dashboard(data):
    name = data.get('name', 'Unknown')
    main = data.get('main', {})
    wind = data.get('wind', {})
    weather = data.get('weather', [{}])[0].get('main', 'N/A')
    desc = data.get('weather', [{}])[0].get('description', 'N/A')

    print('\n' + '=' * 40)
    print(f" Weather Dashboard - {name} ")
    print('=' * 40)
    print(dashboard_line('Temperature', f"{main.get('temp', 'N/A')} °C"))
    print(dashboard_line('Humidity', f"{main.get('humidity', 'N/A')} %"))
    print(dashboard_line('Wind Speed', f"{wind.get('speed', 'N/A')} m/s"))
    print(dashboard_line('Condition', f"{weather} - {desc}"))
    print('=' * 40 + '\n')


def main():
    print('Weather Dashboard')
    try:
        api_key = get_api_key()
        if not api_key:
            print('API key required. Exiting.')
            return
        city = input('Enter city name: ').strip()
        data = fetch_weather(city, api_key)
        display_dashboard(data)
    except requests.HTTPError as he:
        print(f'HTTP error: {he}')
    except requests.RequestException as re:
        print(f'Network error: {re}')
    except Exception as exc:
        print(f'Error: {exc}')


if __name__ == '__main__':
    main()
