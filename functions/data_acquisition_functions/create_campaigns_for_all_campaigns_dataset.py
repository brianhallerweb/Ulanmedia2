from config.config import *
from functions.data_acquisition_functions.get_all_campaign_conversions_by_traffic_source import get_all_campaign_conversions_by_traffic_source
from functions.data_acquisition_functions.get_mgid_campaign_costs import get_mgid_campaign_costs
from functions.classification_functions.classify_campaign_for_all_campaigns import classify_campaign_for_all_campaigns
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.misc.create_mgid_date_range import create_mgid_date_range
import json
import sys
import re
import os

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago, output_name):
    vol_dates = create_vol_date_range(days_ago, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    mgid_dates = create_mgid_date_range(days_ago, mgid_timezone)
    mgid_start_date = mgid_dates[0]
    mgid_end_date = mgid_dates[1]

    # get leads, sales, and revenue by campaign from voluum 
    vol_campaign_data = get_all_campaign_conversions_by_traffic_source(vol_token,
                                                       mgidVolTrafficSourceId
                                                       , vol_start_date, vol_end_date)
    # get clicks, imps, and cost by campaign from mgid
    mgid_campaign_data = get_mgid_campaign_costs(mgid_token, mgid_client_id,
                                              mgid_start_date,
                                              mgid_end_date)["campaigns-stat"]

    # get campaign_sets
    campaign_sets = get_campaign_sets() 

    # create an dictionary to hold data and metadata
    # the metadata is for request dates
    # the data is an array of dicts where each dict is a campaign
    # the stats in each campaign come from both mgid and voluum
    # the campaign data is only collected for campains in campaign_sets.txt
    
    campaigns_data = {"metadata": {"mgid_start_date": mgid_start_date,
                                   "mgid_end_date": mgid_end_date, 
                                   "vol_start_date": vol_start_date,
                                   "vol_end_date": vol_end_date,},
                      "data": []
                      }

    pattern = re.compile(r'.*cpc_(.*)')
    for row in campaign_sets:
        # extract the data out of a single campaign 
        mgid_campaign_id = row["mgid_id"]
        vol_campaign_id = row["vol_id"]
        campaign_name = row["name"]
        pattern = re.compile(r'\d+.\d+')
        res = pattern.findall(campaign_name)
        bid = float(list(res)[0])
        max_lead_cpa = row["max_lead_cpa"]
        max_sale_cpa = row["max_sale_cpa"]
        res = pattern.findall(campaign_name)
        max_cpc = list(res)[0]

        # create an empty dict to hold the final data for a single campaign
        campaign_data = {}

        # fill in the single campaign data
        # some data comes from campaigns_sets.txt
        # some data comes from mgid
        # some data comes from vol
        campaign_data["mgid_id"] = mgid_campaign_id
        campaign_data["vol_id"] = vol_campaign_id
        campaign_data["name"] = campaign_name
        campaign_data["bid"] = bid
        campaign_data["max_lead_cpa"] = max_lead_cpa
        campaign_data["max_sale_cpa"] = max_sale_cpa
        campaign_data["max_cpc"] = max_cpc
        campaign_data["clicks"] = mgid_campaign_data[mgid_campaign_id]["clicks"]
        campaign_data["imps"] = mgid_campaign_data[mgid_campaign_id]["imps"]
        campaign_data["cost"] = mgid_campaign_data[mgid_campaign_id]["spent"]
        if vol_campaign_id in vol_campaign_data:
            campaign_data["leads"] = vol_campaign_data[vol_campaign_id]["leads"]
            campaign_data["sales"] = vol_campaign_data[vol_campaign_id]["sales"]
            campaign_data["revenue"] = vol_campaign_data[vol_campaign_id]["revenue"]
        else:
            campaign_data["leads"] = 0
            campaign_data["sales"] = 0
            campaign_data["revenue"] = 0
        campaigns_data["data"].append(campaign_data)

    for campaign in campaigns_data["data"]:
        campaign["classification"] = classify_campaign_for_all_campaigns(campaign)

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/campaigns_for_all_campaigns/{output_name}.json", "w") as file:
        json.dump(campaigns_data, file)

    print(f"{output_name} created")




