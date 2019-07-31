from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets 
import json
import os
import sys

def create_campaigns_for_one_offer_dataset(date_range, offer_id):

    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["vol_id"]] = campaign["name"]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_campaign/{date_range}_offers_for_each_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    campaigns_for_one_offer = {"metadata": metadata, "data": []}   

    for campaign in data:
        for offer in data[campaign]:
            if offer == offer_id:
                campaigns_for_one_offer["data"].append(data[campaign][offer])

    for campaign in campaigns_for_one_offer["data"]:
        name = campaigns_lookup[campaign["campaign_id"]]
        campaign["campaign_name"] = name

        profit = campaign["profit"]
        cost = campaign["cost"]
        if cost == 0:
            campaign["roi"] = 0
        else:
            campaign["roi"] = profit/cost

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/campaigns_for_one_offer/{offer_id}_{date_range}_campaigns_for_one_offer_dataset.json", "w") as file:
        json.dump(campaigns_for_one_offer, file)
    
    return json.dumps(campaigns_for_one_offer)

