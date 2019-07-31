from config.config import *
import json
import sys
import os

def create_campaigns_for_one_ad_dataset(ad_image, date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_ads/{date_range}_complete_ads_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    campaigns_for_one_ad = {"metadata": metadata, "data": data[ad_image]["for_each_campaign"]}   

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/campaigns_for_one_ad/{ad_image}_{date_range}_campaigns_for_one_ad_dataset.json", "w") as file:
        json.dump(campaigns_for_one_ad, file)

    return json.dumps(campaigns_for_one_ad)


    









