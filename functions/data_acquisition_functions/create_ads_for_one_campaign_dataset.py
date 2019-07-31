from config.config import *
import json
import sys
import os


def create_ads_for_one_campaign_dataset(vol_id, date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_ads/{date_range}_complete_ads_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    ads_for_one_campaign = {"metadata": metadata, "data": []}   

    for ad_image in data.values():
        for ad in ad_image["for_each_campaign"]:
            if vol_id == ad["vol_id"]:
                ads_for_one_campaign["data"].append(ad)
        
    # add the parent ad global rank
    for ad in ads_for_one_campaign["data"]:
        ad_image = ad["image"]
        ad["global_rank"] = data[ad_image]["for_all_campaigns"]["global_rank"]
        ad["global_rank_order"] = data[ad_image]["for_all_campaigns"]["global_rank_order"]

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/ads_for_one_campaign/{vol_id}_{date_range}_ads_for_one_campaign_dataset.json", "w") as file:
        json.dump(ads_for_one_campaign, file)

    return json.dumps(ads_for_one_campaign)


    









