from config.config import *
import json
import sys
import os

def create_languages_for_one_campaign_dataset(date_range, vol_id):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_languages/{date_range}_complete_languages_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    languages_for_one_campaign = {"metadata": metadata, "data": []}   

    for language in data:
        for campaign in data[language]["for_each_campaign"]:
            if data[language]["for_each_campaign"][campaign]["campaign_id"] == vol_id:
                languages_for_one_campaign["data"].append(data[language]["for_each_campaign"][campaign])
        
    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/languages_for_one_campaign/{date_range}_{vol_id}_languages_for_one_campaign_dataset.json", "w") as file:
        json.dump(languages_for_one_campaign, file)

    return json.dumps(languages_for_one_campaign) 

    









