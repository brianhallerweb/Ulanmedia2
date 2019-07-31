from config.config import *
import json
import sys
import os
from functions.classification_functions.classify_offer_for_all_campaigns import classify_offer_for_all_campaigns

def create_offers_for_one_flow_rule_dataset(date_range, flow_rule_argument):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_flow_rule/{date_range}_offers_for_each_flow_rule_dataset.json', 'r') as file:
        json_file = json.load(file)
        
    metadata = json_file["metadata"]
    offers_for_each_flow_rule = json_file["data"]

    offers_for_one_flow_rule = {"metadata": metadata, "data": offers_for_each_flow_rule[flow_rule_argument]}   

    #######################################################
    # Add classification to each offer
    for offer in offers_for_one_flow_rule["data"]:
        offers_for_one_flow_rule["data"][offer]["classification"] = classify_offer_for_all_campaigns(offers_for_one_flow_rule["data"][offer])

    #######################################################
    # Add has_mismatch_vol_weight_and_rec_weight to each offer
    for offer in offers_for_one_flow_rule["data"]:
        vol_weight = offers_for_one_flow_rule["data"][offer]["vol_weight"]
        rec_weight = offers_for_one_flow_rule["data"][offer]["rec_weight"]
        if (vol_weight != rec_weight) & (vol_weight != "NA"):
            offers_for_one_flow_rule["data"][offer]["has_mismatch_vol_weight_and_rec_weight"] = True 
        else:
            offers_for_one_flow_rule["data"][offer]["has_mismatch_vol_weight_and_rec_weight"]  = False

    ###############################################
    # Save file and return 

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/offers_for_one_flow_rule/{flow_rule_argument}_{date_range}_offers_for_one_flow_rule_dataset.json", "w") as file:
        json.dump(offers_for_one_flow_rule, file)
    
    return json.dumps(offers_for_one_flow_rule)

