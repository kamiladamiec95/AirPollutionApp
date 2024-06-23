import os
from dotenv import load_dotenv
import json
import requests

load_dotenv('secrets/.env')
OPENWEATHER_KEY_API = os.environ['OPENWEATHER_API_KEY']

def get_city_coordinates(city):
    """Function returns tuple of city coordinates (latitude, longitude) with use of openweatherAPI
    (https://openweathermap.org/api/geocoding-api)
    """

    GEO_DIRECT_URL = 'http://api.openweathermap.org/geo/1.0/direct?'
    url = f'{GEO_DIRECT_URL}q={city},PL&appid={OPENWEATHER_KEY_API}'
    r = requests.get(url)
    lat = json.loads(r.text)[0]['lat']
    lon = json.loads(r.text)[0]['lon']
    return lat, lon

def get_cities_pollution():
    AIR_POLLUTION_URL = 'http://api.openweathermap.org/data/2.5/air_pollution?'
    f = open('../config.json') 
    cities = json.load(f)['cities'] 
    cities_cord = {}

    for city in cities:
        lat, lon = get_city_coordinates(city)
        cities_cord[city] = lat, lon

    cities_pollution = {}
    for city, city_cord in cities_cord.items():
        r = requests.get(f"{AIR_POLLUTION_URL}lat={city_cord[0]}&lon={city_cord[1]}&appid={OPENWEATHER_KEY_API}")
        cities_pollution[city] = json.loads(r.text)['list'][0]['components']
        
    return cities_pollution

print(get_cities_pollution())
