"""
Project Title: API Data Parser (JSON Parsing)

Project Description:
Fetch JSON data from a sample API (OpenWeatherMap or any accessible JSON URL),
convert it to Python dict and extract useful fields, demonstrating JSON parsing.

Concepts Used:
- requests for HTTP
- JSON handling
- Pretty printing

Sample Input:
Enter URL or press Enter to fetch weather for London (requires API key)

Sample Output:
Keys extracted and pretty-printed JSON snippet

Run:
python api_data_parser.py
"""

import json
import os
from pprint import pprint
import requests


def fetch_json(url: str, params: dict = None, timeout: int = 10):
    """Fetch JSON from a URL and return Python object."""
    resp = requests.get(url, params=params, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def pretty_print_json(obj):
    print('\nPretty JSON output:')
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def parse_openweather_example(api_key: str, city: str = 'London'):
    """Example: fetch weather for a city and extract fields."""
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    data = fetch_json(url, params=params)
    # Extract useful fields
    info = {
        'city': data.get('name'),
        'coordinates': data.get('coord'),
        'temperature': data.get('main', {}).get('temp'),
        'humidity': data.get('main', {}).get('humidity'),
        'weather': data.get('weather', [{}])[0].get('description')
    }
    return data, info


def main():
    print('API Data Parser')
    try:
        user_url = input('Enter a JSON API URL or press Enter to use OpenWeatherMap example: ').strip()
        if user_url:
            data = fetch_json(user_url)
            print('Top-level keys:')
            pprint(list(data.keys()) if isinstance(data, dict) else type(data))
            pretty_print_json(data)
        else:
            api_key = os.getenv('OPENWEATHER_API_KEY') or input('Enter OpenWeatherMap API key: ').strip()
            data, info = parse_openweather_example(api_key)
            print('\nExtracted fields:')
            pprint(info)
            pretty_print_json({k: data[k] for k in ('coord', 'main', 'weather') if k in data})

    except requests.HTTPError as he:
        print(f'HTTP Error: {he}')
    except requests.RequestException as re:
        print(f'Network Error: {re}')
    except Exception as exc:
        print(f'Error: {exc}')


if __name__ == '__main__':
    main()
