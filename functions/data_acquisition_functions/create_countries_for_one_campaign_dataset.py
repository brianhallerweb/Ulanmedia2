from config.config import *
import json
import sys
import os

def create_countries_for_one_campaign_dataset(date_range, vol_id):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_countries/{date_range}_complete_countries_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    countries_for_one_campaign = {"metadata": metadata, "data": []}   

    for country in data:
        for campaign in data[country]["for_each_campaign"]:
            if data[country]["for_each_campaign"][campaign]["campaign_id"] == vol_id:
                countries_for_one_campaign["data"].append(data[country]["for_each_campaign"][campaign])
        
    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/countries_for_one_campaign/{date_range}_{vol_id}_countries_for_one_campaign_dataset.json", "w") as file:
        json.dump(countries_for_one_campaign, file)

    return json.dumps(countries_for_one_campaign) 

    









