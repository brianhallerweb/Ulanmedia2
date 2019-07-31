from config.config import *
from functions.misc.send_email import send_email
from datetime import datetime
import requests
import re
import sys
import json

def get_all_campaign_conversions_by_traffic_source(token,
        traffic_source_id, start_date, end_date):
    url=f"https://api.voluum.com/report/conversions?from={start_date}T00%3A00%3A00Z&to={end_date}T00:00:00Z&tz={mgid_timezone}&filter={traffic_source_id}&sort=campaignName&direction=asc&columns=transactionId&columns=revenue&columns=campaignName&columns=trafficSourceId&groupBy=conversion&offset=0&limit=100000&include=ACTIVE&conversionTimeMode=VISIT"
    try:
        campaigns = requests.get(url, headers = {"cwauth-token": token}).json()

        if campaigns["totalRows"] != len(campaigns["rows"]):
            # The get request has a limit of 100,000 so if there are more than 
            # 100,000 conversions returned, this exception will be raised. 
            raise Exception("voluum didn't return all the conversion data.")

        # create a dictionary to hold the conversion and revenue data for each
        # campaign. Fill the empty campaigns_data with key = vol_id and value =
        # dict with name, revenue, leads, and sales keys. 
        campaigns_data = {} 
        for campaign in campaigns["rows"]:
            vol_id = campaign["campaignId"]
            campaign_name = re.sub(r"^.* - ", "",campaign["campaignName"], count=1)        
            if vol_id not in campaigns_data:
                campaigns_data[vol_id] = {"name": campaign_name, "revenue": 0,
                        "leads": 0, "sales": 0}

        for campaign in campaigns["rows"]:
            # check that visitTimestamp is within the date range of choice.
            # This is necessary because the request returns results based on
            # the sale date, not the original click date. We only want results
            # where the original click date is within the chosen date range. 
            start_date_in_date_format = datetime.strptime(start_date, "%Y-%m-%d")
            click_date_in_date_format = datetime.strptime(campaign["visitTimestamp"], "%Y-%m-%d %I:%M:%S %p")
            if start_date_in_date_format > click_date_in_date_format:
                continue

            revenue = campaign["revenue"]
            vol_id = campaign["campaignId"]
            campaign_name = re.sub(r"^.* - ", "",campaign["campaignName"], count=1)        
            lead = 0
            sale = 0
            if campaign["transactionId"] == "account":
                lead = 1
            elif campaign["transactionId"] == "deposit":
                sale = 1
            campaigns_data[vol_id]["leads"] += lead
            campaigns_data[vol_id]["sales"] += sale
            campaigns_data[vol_id]["revenue"] += revenue 
        return campaigns_data 
    except requests.exceptions.RequestException as e:
        print("Failed - get_all_campaign_conversions_by_traffic_source()") 
        send_email("brianshaller@gmail.com", "Failed - get_all_campaign_conversions_by_traffic_source at " +
                str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()
