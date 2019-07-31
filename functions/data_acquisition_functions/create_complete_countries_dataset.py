from config.config import *
from functions.classification_functions.classify_country import classify_country
import sys
import json
import os

def create_complete_countries_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/countries/{date_range}_countries_dataset.json', 'r') as file:
        json_file = json.load(file)


    complete_countries = {"metadata": {"vol_start_date": json_file["metadata"]["vol_start_date"],
                                 "vol_end_date": json_file["metadata"]["vol_end_date"],
                                 },
                    "data": {}
                   }

    for country_name in json_file["data"]:
        for campaign_id in json_file["data"][country_name]:
            if country_name not in complete_countries["data"]:
                complete_countries["data"][country_name] = {
                        # 4/5/19 "for_all_campaigns" has the first campaign_id in it
                        # and it shouldn't have a campaign_id because its for
                        # all campaigns. Fix this later. 
                        "for_all_campaigns": json_file["data"][country_name][campaign_id],
                        "for_each_campaign": {}}
            else:
                complete_countries["data"][country_name]["for_all_campaigns"]["clicks"] += json_file["data"][country_name][campaign_id]["clicks"]
                complete_countries["data"][country_name]["for_all_campaigns"]["conversions"] += json_file["data"][country_name][campaign_id]["conversions"]
                complete_countries["data"][country_name]["for_all_campaigns"]["leads"] += json_file["data"][country_name][campaign_id]["leads"]
                complete_countries["data"][country_name]["for_all_campaigns"]["sales"] += json_file["data"][country_name][campaign_id]["sales"]
                complete_countries["data"][country_name]["for_all_campaigns"]["profit"] += json_file["data"][country_name][campaign_id]["profit"]
                complete_countries["data"][country_name]["for_all_campaigns"]["cost"] += json_file["data"][country_name][campaign_id]["cost"]
                complete_countries["data"][country_name]["for_all_campaigns"]["revenue"] += json_file["data"][country_name][campaign_id]["revenue"]

    # the json_file needs to be loaded again because it mutates during the
    # previous accumulation step
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/countries/{date_range}_countries_dataset.json', 'r') as file:
        json_file = json.load(file)

    for country_name in json_file["data"]:
        for campaign_id in json_file["data"][country_name]:
            complete_countries["data"][country_name]["for_each_campaign"][campaign_id] = json_file["data"][country_name][campaign_id]

    for country_name in complete_countries["data"]:
        complete_countries["data"][country_name]["for_all_campaigns"]["classification"] = classify_country(complete_countries["data"][country_name]["for_all_campaigns"])

    for country_name in complete_countries["data"]:
        for campaign in complete_countries["data"][country_name]["for_each_campaign"]:
            complete_countries["data"][country_name]["for_each_campaign"][campaign]["classification"] = classify_country(complete_countries["data"][country_name]["for_each_campaign"][campaign])

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/complete_countries/{date_range}_complete_countries_dataset.json", "w") as file:
        json.dump(complete_countries, file)




