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
    # print(dict_data, type(dict_data))
    print(data)
    return str(True)


## melt w pandasie
## jak to wstawic do bigquery