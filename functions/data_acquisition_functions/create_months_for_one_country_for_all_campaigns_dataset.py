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

def create_months_for_one_country_for_all_campaigns_dataset(token, start_date, end_date, country_name):

    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    
    months = {"metadata": {"vol_start_date": start_date, "vol_end_date":
        end_date}, "data": {}}

    url = f"https://api.voluum.com/report?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&filter={country_name}&conversionTimeMode=VISIT&currency=USD&sort=month&direction=asc&columns=month&columns=countryName&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cv&columns=roi&columns=epv&groupBy=month&groupBy=country-code&offset=0&limit=1000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"
    res = requests.get(url, headers = {"cwauth-token": token}).json()
    for row in res["rows"]:
        month = row["month"]
        clicks = row["visits"]
        cost = row["cost"]
        revenue = row["revenue"]
        profit = row["profit"]
        month_index = find_month_index_number(month)

        months["data"][month] = {"month": month, "month_index": month_index, "clicks": clicks, "cost": cost,
                "revenue": revenue, "profit": profit, "leads": 0, "sales": 0} 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/conversions_for_each_campaign/oneeighty_conversions_for_each_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    conversions_for_each_campaign = json_file["data"]

    for campaign in conversions_for_each_campaign:
        for conversion in conversions_for_each_campaign[campaign]:
            country = conversion["countryName"].lower()
            if country != country_name:
                continue
            month = int(conversion["visitTimestamp"].split('-')[1])
            conversion_type = conversion["transactionId"]
            if conversion_type == "account":
                if month in months["data"]:
                    months["data"][month]["leads"] += 1
            elif conversion_type == "deposit":
                if month in months["data"]:
                    months["data"][month]["sales"] += 1

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/months_for_one_country_for_all_campaigns/{country_name}_months_for_one_country_for_all_campaigns_dataset.json", "w") as file:
        json.dump(months, file)

    return json.dumps(months)

