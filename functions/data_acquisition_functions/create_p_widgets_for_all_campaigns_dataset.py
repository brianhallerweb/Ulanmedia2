from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets 
import re
import os
import sys
import json

def create_p_widgets_for_all_campaigns_dataset(date_range):

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
        complete_p_widgets = json.load(file)
    
    ########################################################

    # 2. set up the basic data structure you want to create

    p_widgets_for_all_campaigns = {"metadata":{}, "data":{}}

    #########################################################

    # 3. Add the metadata. The metadata are the date ranges of the mgid and vol
    # request dates. All p_and_c_widgets_for_one_campaign files have the same
    # date ranges so I am just using the first campaign. 

    vol_id_for_adding_metadata = campaigns[0]["vol_id"]
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    p_widgets_for_all_campaigns["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    p_widgets_for_all_campaigns["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    p_widgets_for_all_campaigns["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    p_widgets_for_all_campaigns["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    #########################################################

    # 4. Add the data

    p_widgets_for_all_campaigns["data"] = complete_p_widgets

    #########################################################

    # 5. remove "for_each_campaign" "good_campaigns_count" "bad_campaigns_count" and 
    # "wait_campaigns_count" from each widget and add "good_campaigns_count" "bad_campaigns_count"
    # and "wait_campaigns_count" to p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]
    for p_widget in p_widgets_for_all_campaigns["data"]:
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["good_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["bad_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["wait_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget] = p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]
    
    ############################################################
    # 6. Save p_widgets_for_all_campaigns to a json file and return it as a
    # json file 

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/p_widgets_for_all_campaigns/{date_range}_p_widgets_for_all_campaigns_dataset.json", "w") as file:
        json.dump(p_widgets_for_all_campaigns, file)

    return json.dumps(p_widgets_for_all_campaigns)

