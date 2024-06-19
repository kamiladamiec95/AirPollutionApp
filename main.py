import functions_framework
import sys
import os
import json
import ast
import base64
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # add gcloud_functions
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # add gcloud



# PLIK CONFIG
# WYCIAGNAC LAT I LONG
# NA PODSTAWIE TEGO AIR POLLUTION
    
@functions_framework.http
def gcloud_get_openweather_data_function(request, context=None) -> str:
    return 'helloworld'