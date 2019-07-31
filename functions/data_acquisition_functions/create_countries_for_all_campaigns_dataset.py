from config.config import *
import json
import os
import sys

def create_countries_for_all_campaigns_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_countries/{date_range}_complete_countries_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    countries_for_all_campaigns = {"metadata": metadata, "data": []}   
    for country_name in data:
        countries_for_all_campaigns["data"].append(data[country_name]["for_all_campaigns"])

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/countries_for_all_campaigns/{date_range}_countries_for_all_campaigns_dataset.json", "w") as file:
        json.dump(countries_for_all_campaigns, file)
    
    return json.dumps(countries_for_all_campaigns)


    









