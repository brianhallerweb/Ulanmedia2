from config.config import *
from functions.data_acquisition_functions.get_vol_daily_stats_data import get_vol_daily_stats_data
from functions.data_acquisition_functions.get_mgid_daily_stats_data import get_mgid_daily_stats_data
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.send_email import send_email
from datetime import datetime, timedelta
import json
import re
import pytz
import sys

# This function will create a json data set where each key is a vol campaign id
# and each value is a list of dictionaries, where is dictionary is a collection
# of daily stats for one day. Only use this function if you want to create a 
# dataset with all 50 days. To update an existing data set with new daily stats for
# yesterday (and delete the daily stats for 51 days ago) use
# add_yesterday_in_days_for_one_campaign_dataset()

def create_days_for_one_campaign_dataset(vol_token, mgid_token, days_ago, 
        output_name):
    
    # create campaigns lookup dictionary so that you can find the corresponding
    # mgid_id from the vol_id
    # keys are vol_id, values are mgid_id
    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["vol_id"]] = campaign["mgid_id"]
        
    # set up the dictionary to store daily stats by campaign
    # keys are vol_id, values are empty lists that will be filled
    # with a dictionaries of daily stats
    daily_stats= {}
    for campaign in campaigns_sets:
        daily_stats[campaign["vol_id"]] = []
    
     # fill the dictionary with data from each day
    for i in range(1, days_ago + 1):
        # create vol dates
        # to get yesterday's daily stats, vol_start_date is yesterday and 
        # vol_end_date is today
        start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(i)
        start_date_pst = start_date_utc.astimezone(pytz.timezone(mgid_timezone))
        end_date_utc = pytz.utc.localize(datetime.utcnow() - timedelta(i - 1)) 
        end_date_pst = end_date_utc.astimezone(pytz.timezone(mgid_timezone))
        vol_start_date = start_date_pst.strftime("%Y-%m-%d")
        vol_end_date = end_date_pst.strftime("%Y-%m-%d")
    
        # create mgid dates 
        # to get yesterday's daily stats, mgid_start_date is yesterday and 
        # mgid_end_date is yesterday 
        start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(i)
        start_date_pst = start_date_utc.astimezone(pytz.timezone(mgid_timezone))
        mgid_start_date = start_date_pst.strftime("%Y-%m-%d")
        mgid_end_date = mgid_start_date

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

    # create a json file
    with open(f"../../data/days_for_one_campaign/{output_name}.json", "w") as file:
          json.dump(daily_stats, file)

    print(f"{output_name} created")
