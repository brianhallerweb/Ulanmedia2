from config.config import *
from functions.classification_functions.classify_language import classify_language
import sys
import json
import os

def create_complete_languages_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/languages/{date_range}_languages_dataset.json', 'r') as file:
        json_file = json.load(file)


    complete_languages = {"metadata": {"vol_start_date": json_file["metadata"]["vol_start_date"],
                                 "vol_end_date": json_file["metadata"]["vol_end_date"],
                                 },
                    "data": {}
                   }

    for language_name in json_file["data"]:
        for campaign_id in json_file["data"][language_name]:
            if language_name not in complete_languages["data"]:
                complete_languages["data"][language_name] = {
                        "for_all_campaigns": json_file["data"][language_name][campaign_id],
                        "for_each_campaign": {}}
            else:
                complete_languages["data"][language_name]["for_all_campaigns"]["clicks"] += json_file["data"][language_name][campaign_id]["clicks"]
                complete_languages["data"][language_name]["for_all_campaigns"]["conversions"] += json_file["data"][language_name][campaign_id]["conversions"]
                complete_languages["data"][language_name]["for_all_campaigns"]["profit"] += json_file["data"][language_name][campaign_id]["profit"]
                complete_languages["data"][language_name]["for_all_campaigns"]["cost"] += json_file["data"][language_name][campaign_id]["cost"]
                complete_languages["data"][language_name]["for_all_campaigns"]["revenue"] += json_file["data"][language_name][campaign_id]["revenue"]

    # the json_file needs to be loaded again because it mutates during the
    # previous accumulation step
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/languages/{date_range}_languages_dataset.json', 'r') as file:
        json_file = json.load(file)

    for language_name in json_file["data"]:
        for campaign_id in json_file["data"][language_name]:
            complete_languages["data"][language_name]["for_each_campaign"][campaign_id] = json_file["data"][language_name][campaign_id]

    for language_name in complete_languages["data"]:
        complete_languages["data"][language_name]["for_all_campaigns"]["classification"] = classify_language(complete_languages["data"][language_name]["for_all_campaigns"])

    for language_name in complete_languages["data"]:
        for campaign in complete_languages["data"][language_name]["for_each_campaign"]:
            complete_languages["data"][language_name]["for_each_campaign"][campaign]["classification"] = classify_language(complete_languages["data"][language_name]["for_each_campaign"][campaign])

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/complete_languages/{date_range}_complete_languages_dataset.json", "w") as file:
        json.dump(complete_languages, file)




