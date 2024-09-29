import functions_framework
import sys
import os
import json
import ast
import base64
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # add gcloud_functions
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # add gcloud
from src.extract import get_cities_pollution_history
from src.extract import get_cities_pollution_history
import src.transform
import pandas as pd


# PLIK CONFIG
# WYCIAGNAC LAT I LONG
# NA PODSTAWIE TEGO AIR POLLUTION
    
@functions_framework.http
def gcloud_get_openweather_data_function(request, context=None) -> str:
    pollution = get_cities_pollution_history('config.json')
    return str(pollution)



@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    # Print out the data from Pub/Sub, to prove that it worked
    data = src.transform.convert_pandas(base64.b64decode(cloud_event.data["message"]["data"]))
    return str(True)

@functions_framework.http
def test_function(request, context=None) -> str:
    pollution = get_cities_pollution_history('config.json')
    dict_data = ast.literal_eval(str(pollution))
    json_str = json.dumps(dict_data)
    data = src.transform.convert_pandas(json.loads(json_str))
    data = pd.melt(data)
    # data = data['value']
    # data = pd.json_normalize(data)
    data = data.join(pd.json_normalize(data.pop('value')))
    # data['ColumnA'] = data[data.columns[1:]].apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)
    # print(dict_data, type(dict_data))
    # data.melt('variable', value_name='dt')
    # data = pd.melt(data, id_vars=['variable'], value_vars=['dt', 'main.aqi', 'components.co', 'components.no', 'components.no2', 'components.o3', 'components.so2', 'components.pm2_5', 'components.pm10', 'components.nh3'])
    data = data.stack().reset_index()
    print(data.to_string())
    return str(True)


## melt w pandasie
## jak to wstawic do bigquery