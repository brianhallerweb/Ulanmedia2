from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.find_month_index_number import find_month_index_number
from datetime import datetime
from datetime import datetime, timedelta
import requests
import json
import sys
import re
import os

def create_months_for_one_ad_for_one_campaign_dataset(token, start_date, end_date, ad_image, campaign_id):
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    
    months = {"metadata": {"vol_start_date": start_date, "vol_end_date":
        end_date}, "data": {}}
    url = f"https://api.voluum.com/report?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&filter={ad_image}&conversionTimeMode=VISIT&currency=USD&sort=month&direction=desc&columns=month&columns=customVariable5&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cv&columns=roi&columns=epv&groupBy=month&groupBy=custom-variable-5&offset=0&limit=1000&include=ACTIVE&filter1=campaign&filter1Value={campaign_id}"
    res = requests.get(url, headers = {"cwauth-token": token}).json()
    for row in res["rows"]:
        month = row["month"]
        clicks = row["visits"]
        cost = row["cost"]
        revenue = row["revenue"]
        profit = row["profit"]
        if month in months["data"]:
            months["data"][month]["clicks"] += clicks
            months["data"][month]["cost"] += cost
            months["data"][month]["revenue"] += revenue 
            months["data"][month]["profit"] += profit
        else:
            months["data"][month] = {"clicks": clicks,
                    "cost": cost, 
                    "revenue": revenue, 
                    "profit": profit, 
                    "leads": 0,
                    "sales": 0,
                    "month": month,
                    "month_index": find_month_index_number(month)

                    }

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/conversions_for_each_campaign/oneeighty_conversions_for_each_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    conversions_for_each_campaign = json_file["data"]

    for conversion in conversions_for_each_campaign[campaign_id]:
        ad = conversion["customVariable5"]
        if ad != ad_image:
            continue
        month = int(conversion["visitTimestamp"].split('-')[1])
        conversion_type = conversion["transactionId"]
        if conversion_type == "account":
            if month in months["data"]:
                months["data"][month]["leads"] += 1
        elif conversion_type == "deposit":
            if month in months["data"]:
                months["data"][month]["sales"] += 1

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/months_for_one_ad_for_one_campaign/{ad_image}_{campaign_id}_months_for_one_ad_for_one_campaign_dataset.json", "w") as file:
        json.dump(months, file)

    return json.dumps(months)


