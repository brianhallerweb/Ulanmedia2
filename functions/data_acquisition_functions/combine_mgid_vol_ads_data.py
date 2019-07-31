from config.config import *
from functions.data_acquisition_functions.get_mgid_ads_data import get_mgid_ads_data
from functions.data_acquisition_functions.get_vol_ads_data import get_vol_ads_data
from functions.classification_functions.classify_p_and_c_ads import classify_p_and_c_ads
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.misc.get_campaign_sets import get_campaign_sets
import sys
import json
import os


def combine_mgid_vol_ads_data(mgid_token, vol_token, date_range, vol_start_date,
        vol_end_date, mgid_data, vol_data):
    # This function will combine the mgid ads data and the vol ads data. Both
    # data sets are dictionaries with keys = ad id and values = dictionaries of
    # data for that ad id. 

    # create a look up dictionary so you can find vol id, and campaign name from mgid id
    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["mgid_id"]] = [campaign["vol_id"],
        campaign["name"]]
    
    # combining mgid and vol by ad_id
    combined_ads = {"metadata": {"vol_start_date": vol_start_date,
                                 "vol_end_date": vol_end_date
                                 },
                    "data": {}
                   }

    for ad in mgid_data.values():
        ad_id = ad["ad_id"]  
        mgid_id = ad["mgid_id"]
        if mgid_id not in campaigns_lookup:
            continue
        vol_id = campaigns_lookup[mgid_id][0]
        name = campaigns_lookup[mgid_id][1]
        if ad_id in vol_data:
            vol_ad_data = vol_data[ad_id]
            ad["vol_id"] = vol_id
            ad["name"] = name
            ad["conversions"] = vol_ad_data["conversions"]
            ad["sales"] = vol_ad_data["sales"]
            ad["leads"] = vol_ad_data["leads"]
            ad["revenue"] = vol_ad_data["revenue"]
        else:
            ad["vol_id"] = vol_id
            ad["name"] = name
            ad["conversions"] = 0
            ad["sales"] = 0
            ad["leads"] = 0
            ad["revenue"] = 0 
        combined_ads["data"][ad_id] = ad 

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/ads/{date_range}_ads_dataset.json", "w") as file:
        json.dump(combined_ads, file)
 


