from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets
from datetime import datetime
from datetime import datetime, timedelta
import requests
import json
import sys
import os
import re

def create_days_for_one_offer_for_all_campaigns_dataset(token, start_date,
        end_date, offer_name):
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    
    days = {"metadata": {"vol_start_date": start_date, "vol_end_date":
        end_date}, "data": {}}

    url = f"https://api.voluum.com/report?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&filter={offer_name}&conversionTimeMode=VISIT&currency=USD&sort=day&direction=desc&columns=day&columns=offerName&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cv&columns=roi&columns=epv&groupBy=day&groupBy=offer&offset=0&limit=1000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"
    res = requests.get(url, headers = {"cwauth-token": token}).json()
    for row in res["rows"]:
        day = row["day"]
        clicks = row["visits"]
        cost = row["cost"]
        revenue = row["revenue"]
        profit = row["profit"]
        days["data"][day] = {"day": day, "clicks": clicks, "cost": cost,
                "revenue": revenue, "profit": profit, "leads": 0, "sales": 0} 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/conversions_for_each_campaign/oneeighty_conversions_for_each_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    conversions_for_each_campaign = json_file["data"]

    offer_pattern = re.compile(r'(\w* - \w* - )(.*)')

    for campaign in conversions_for_each_campaign:
        for conversion in conversions_for_each_campaign[campaign]:
            offer = list(offer_pattern.findall(conversion["offerName"])[0])[1]
            if offer != offer_name:
                continue
            day = conversion["visitTimestamp"].split(' ')[0] 
            conversion_type = conversion["transactionId"]
            if conversion_type == "account":
                if day in days["data"]:
                    days["data"][day]["leads"] += 1
            elif conversion_type == "deposit":
                if day in days["data"]:
                    days["data"][day]["sales"] += 1

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/days_for_one_offer_for_all_campaigns/{offer_name}_days_for_one_offer_for_all_campaigns_dataset.json", "w") as file:
        json.dump(days, file)

    return json.dumps(days)


