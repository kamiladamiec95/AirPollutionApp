import os
from dotenv import load_dotenv
import json
import requests


def get_data_open_weather_API():
    load_dotenv('secrets/.env')
    openweather_key_api = os.environ['OPENWEATHER_API_KEY']
    GEO_DIRECT_URL = 'http://api.openweathermap.org/geo/1.0/direct?'
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid={openweather_key_api}"
    url2 = f"{GEO_DIRECT_URL}q=Gdansk,PL&appid={openweather_key_api}"
    r = requests.get(url2)
    return json.loads(r.text)


print(get_data_open_weather_API())