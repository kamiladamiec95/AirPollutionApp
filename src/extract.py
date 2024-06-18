import os
from dotenv import load_dotenv
import json
import requests


def get_data_open_weather_API():
    load_dotenv('secrets/.env')
    openweather_key_api = os.environ['OPENWEATHER_API_KEY']

    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid={openweather_key_api}"
    r = requests.get(url)
    return json.loads(r.text)