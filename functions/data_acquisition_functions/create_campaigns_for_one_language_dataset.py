from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets
import json
import sys
import os

def create_campaigns_for_one_language_dataset(date_range, language_name):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_languages/{date_range}_complete_languages_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    campaigns_for_one_language = {"metadata": metadata, "data": data[language_name]["for_each_campaign"]}   

    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["vol_id"]] = campaign["name"]

    for campaign_id in campaigns_for_one_language["data"]:
        campaigns_for_one_language["data"][campaign_id]["campaign_name"] = campaigns_lookup[campaign_id]

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/campaigns_for_one_language/{date_range}_{language_name}_campaigns_for_one_language_dataset.json", "w") as file:
        json.dump(campaigns_for_one_language, file)

    return json.dumps(campaigns_for_one_language)


    









