import os
from dotenv import load_dotenv
import json
import requests
import datetime
import pandas

# przedstawienei tego w dataframe pandas

def get_date():
    date_now = datetime.datetime.now()
    end = date_now.replace(hour=0, minute=0,second=0,microsecond=0)
    start = end - datetime.timedelta(days=1)    
    return int(datetime.datetime.timestamp(start)), int(datetime.datetime.timestamp(end))

# print(get_date())

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
    """Function returns dictionary of city pollution with use of openweatherAPI
    (https://openweathermap.org/api/air-pollution)
    """
    
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


def get_cities_pollution_history():
    """Function returns dictionary of city pollution with use of openweatherAPI
    (https://openweathermap.org/api/air-pollution)
    """
    AIR_POLLUTION_HISTORY_URL = 'http://api.openweathermap.org/data/2.5/air_pollution/history?'
    # AIR_POLLUTION_URL = 'http://api.openweathermap.org/data/2.5/air_pollution?'
    f = open('../config.json') 
    cities = json.load(f)['cities'] 
    cities_cord = {}
    unix_start_date, unix_end_date = get_date()

    for city in cities:
        lat, lon = get_city_coordinates(city)
        cities_cord[city] = lat, lon

    cities_pollution = {}
    for city, city_cord in cities_cord.items():
        r = requests.get(f"{AIR_POLLUTION_HISTORY_URL}lat={lat}&lon={lon}&start={unix_start_date}&end={unix_end_date}&appid={OPENWEATHER_KEY_API}")
        # r = requests.get(f"{AIR_POLLUTION_URL}lat={city_cord[0]}&lon={city_cord[1]}&appid={OPENWEATHER_KEY_API}")
        cities_pollution[city] = json.loads(r.text)['list']
        
    return cities_pollution #['Gdansk']


# print(get_cities_pollution_history())

# df = pandas.DataFrame(columns=['City','co','no','no2','o3','so2','pm2_5', 'pm10', 'nh3'])
l = []

for city, values in get_cities_pollution_history().items():
    # print(city)
    # print(values)
    for i in values:
        i['components']['city'] = city
        l.append(i['components'])
        # for v1 in i['components'].keys():
        #     print(v1)
            # l.append([city,v1,v2])
            # print(l)

df = pandas.DataFrame(l)
print(df)