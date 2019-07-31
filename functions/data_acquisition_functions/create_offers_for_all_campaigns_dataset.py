from config.config import *
from datetime import datetime
import json
import sys
import re
import os
from functions.classification_functions.classify_offer_for_all_campaigns import classify_offer_for_all_campaigns

def create_offers_for_all_campaigns_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_campaign/{date_range}_offers_for_each_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_flow_rule/{date_range}_offers_for_each_flow_rule_dataset.json', 'r') as file:
        json_file = json.load(file)
    offers_for_each_flow_rule = json_file["data"]

    #####################################

    # Create the offers_for_all_campaigns dataset
 
    offers_for_all_campaigns = {"metadata": metadata, "data": {}}   

    for campaign in data:
        for offer in data[campaign]:
            if offer in offers_for_all_campaigns["data"]:
                offers_for_all_campaigns["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                offers_for_all_campaigns["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                offers_for_all_campaigns["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                offers_for_all_campaigns["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 
                offers_for_all_campaigns["data"][offer]["sales"] += data[campaign][offer]["sales"] 
                offers_for_all_campaigns["data"][offer]["leads"] += data[campaign][offer]["leads"] 
                offers_for_all_campaigns["data"][offer]["revenue"] += data[campaign][offer]["revenue"] 
            else:
                offers_for_all_campaigns["data"][offer] = {
                                                          "offer_id": data[campaign][offer]["offer_id"],
                                                          "vol_offer_name": data[campaign][offer]["vol_offer_name"],
                                                          "offer_name": data[campaign][offer]["offer_name"],
                                                          "p_offer_name": data[campaign][offer]["p_offer_name"],
                                                          "c_offer_name": data[campaign][offer]["c_offer_name"],
                                                          "flow_rule": data[campaign][offer]["flow_rule"],
                                                          "flow_rule_index": data[campaign][offer]["flow_rule_index"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                          "cost": data[campaign][offer]["cost"],
                                                          "profit": data[campaign][offer]["profit"], 
                                                          "revenue": data[campaign][offer]["revenue"], 
                                                          "conversions": data[campaign][offer]["conversions"],
                                                          "sales": data[campaign][offer]["sales"],
                                                          "leads": data[campaign][offer]["leads"],
                                                          "rec_weight": offers_for_each_flow_rule[data[campaign][offer]["flow_rule"]][data[campaign][offer]["offer_id"]]["rec_weight"],
                                                          "vol_weight": data[campaign][offer]["vol_weight"],
                                                          "roi_score": offers_for_each_flow_rule[data[campaign][offer]["flow_rule"]][data[campaign][offer]["offer_id"]]["roi_score"],
                                                          "roi": offers_for_each_flow_rule[data[campaign][offer]["flow_rule"]][data[campaign][offer]["offer_id"]]["roi"],
                                                          "cvr_score": offers_for_each_flow_rule[data[campaign][offer]["flow_rule"]][data[campaign][offer]["offer_id"]]["cvr_score"],
                                                          "gpr": offers_for_each_flow_rule[data[campaign][offer]["flow_rule"]][data[campaign][offer]["offer_id"]]["gpr"],
                                                          "total_score": offers_for_each_flow_rule[data[campaign][offer]["flow_rule"]][data[campaign][offer]["offer_id"]]["total_score"],
                                                          }

    #######################################################
    # 7. Add classifcation to each offer
    for offer in offers_for_all_campaigns["data"]:
        offers_for_all_campaigns["data"][offer]["classification"] = classify_offer_for_all_campaigns(offers_for_all_campaigns["data"][offer])

    #######################################################
    # 8. Add has_mismatch_vol_weight_and_rec_weight to each offer
    for offer in offers_for_all_campaigns["data"]:
        vol_weight = offers_for_all_campaigns["data"][offer]["vol_weight"]
        rec_weight = offers_for_all_campaigns["data"][offer]["rec_weight"]
        if (vol_weight != rec_weight) & (vol_weight != "NA"):
            offers_for_all_campaigns["data"][offer]["has_mismatch_vol_weight_and_rec_weight"] = True 
        else:
            offers_for_all_campaigns["data"][offer]["has_mismatch_vol_weight_and_rec_weight"]  = False

    ###############################################
    # 9. Save file and return 

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/offers_for_all_campaigns/{date_range}_offers_for_all_campaigns_dataset.json", "w") as file:
        json.dump(offers_for_all_campaigns, file)
    
    return json.dumps(offers_for_all_campaigns)

