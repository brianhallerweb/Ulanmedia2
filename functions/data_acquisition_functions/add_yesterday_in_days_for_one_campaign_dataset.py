from config.config import *
from functions.data_acquisition_functions.get_vol_daily_stats_data import get_vol_daily_stats_data
from functions.data_acquisition_functions.get_mgid_daily_stats_data import get_mgid_daily_stats_data
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.create_mgid_date_range import create_mgid_date_range
from functions.misc.create_vol_date_range import create_vol_date_range
import json
import os
import re
import sys


def add_yesterday_in_days_for_one_campaign_dataset(vol_token, mgid_token):

    # create campaigns lookup dictionary
    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["vol_id"]] = campaign["mgid_id"]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/days_for_one_campaign/days_for_one_campaign_dataset.json', 'r') as file:
         days_for_one_campaign_dataset = json.load(file)
         

    # create vol dates
    # to get yesterday's daily stats, vol_start_date is yesterday and 
    # vol_end_date is today
    vol_date_range = create_vol_date_range(1, mgid_timezone)
    vol_start_date = vol_date_range[0]
    vol_end_date = vol_date_range[1]

    # create mgid dates 
    # to get yesterday's daily stats, mgid_start_date is yesterday and 
    # mgid_end_date is yesterday 
    mgid_date_range = create_mgid_date_range(1, mgid_timezone)
    mgid_start_date = mgid_date_range[0]
    mgid_end_date = mgid_date_range[1]

    # set up the dictionary to store daily stats by campaign
    # keys are vol_id, values are yesterday's daily stats for that campaign
    daily_stats= {}
    for campaign in campaigns_sets:
        daily_stats[campaign["vol_id"]] = []

    # get vol and mgid data
    vol_response = get_vol_daily_stats_data(vol_token, vol_start_date,
            vol_end_date, mgid_timezone)
    mgid_response = get_mgid_daily_stats_data(mgid_token, mgid_start_date,
            mgid_end_date)
    
    # fill in the daily_stats dictionary
    # each key is a vol campaign id
    # each value is a dictionary of data, some from mgid, some from vol
    # data from mgid
         # clicks
         # cost
    # data from vol
        # conversions
        # revenue
        # name
        # day

    # Some of this code is complicated and going to be very difficult to
    # understand. The reason for all the loops and conditionals is that if
    # a campaign does not have any data for a particular day, voluum
    # returns nothing rather than returning a response that says clicks=0,
    # etc. That is why I had to create lists of campaigns with data and
    # campaigns without data. 
    campaigns_with_day_data = []
    campaigns_without_day_data = []
    day = ""
    for campaign in vol_response:
        vol_id = campaign["campaignId"]
        day = campaign["day"]
        campaigns_with_day_data.append(vol_id)
        # this conditional will exclude vol responses from campaigns that
        # are no longer in campaign_sets.txt
        if vol_id in daily_stats:
            mgid_id = str(campaigns_lookup[vol_id])
            daily_stats[vol_id].append({"vol_id": vol_id,
                    "conversions": campaign["conversions"],
                    "revenue": campaign["revenue"],
                    "name": re.sub(r"^.* - ", "",campaign["campaignName"], count=1),
                    "day": campaign["day"],
                    "clicks": mgid_response[mgid_id]["clicks"],
                    "cost": mgid_response[mgid_id]["spent"],
                        })
    for campaign in daily_stats.keys():
        if campaign not in campaigns_with_day_data:
            campaigns_without_day_data.append(campaign)
    for campaign in campaigns_without_day_data:
        daily_stats[campaign].append({"vol_id": campaign,
               "conversions": 0,
               "revenue": 0,
               "name": "",
               "day": day,
               "clicks": 0,
               "cost": 0,
                   })

    for campaign in days_for_one_campaign_dataset:
        # add daily stats for yesterday
        days_for_one_campaign_dataset[campaign].insert(0,
                daily_stats[campaign][0] )
        # remove daily stats for 50 days ago
        days_for_one_campaign_dataset[campaign].pop()

    # create a json file
    with open(f"../../data/days_for_one_campaign/days_for_one_campaign_dataset.json", "w") as file:
          json.dump(days_for_one_campaign_dataset, file)
    print(f"yesterday's daily stats added to days_for_one_campaign_dataset.json" )
