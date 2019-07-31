from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets
from datetime import datetime
import requests
import sys
import json
import os

def create_conversions_for_each_campaign_dataset(token, start_date, end_date, date_range):
    try:
        url = f"https://api.voluum.com/report/conversions?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&conversionTimeMode=VISIT&sort=visitTimestamp&direction=desc&columns=visitTimestamp&columns=transactionId&columns=campaignId&columns=offerId&columns=countryName&columns=trafficSourceId&columns=deviceName&columns=os&columns=browser&columns=isp&columns=customVariable1&columns=customVariable3&groupBy=conversion&offset=0&limit=1000000&include=ACTIVE&filter=37bbd390-ed90-4978-9066-09affa682bcc"
        res = requests.get(url, headers = {"cwauth-token": token})
        res.raise_for_status()
        res = res.json()
        conversions_for_each_campaign = {"metadata": {"vol_start_date":
            start_date, "vol_end_date": end_date}, "data": {}}
        for conversion in res["rows"]:
            campaign_id = conversion["campaignId"]
            if campaign_id not in conversions_for_each_campaign["data"]:
                conversions_for_each_campaign["data"][campaign_id] = [conversion]
            else:
                conversions_for_each_campaign["data"][campaign_id].append(conversion)
        with open(f"{os.environ.get('ULANMEDIAAPP')}/data/conversions_for_each_campaign/{date_range}_conversions_for_each_campaign_dataset.json", "w") as file:
            json.dump(conversions_for_each_campaign, file)
    
    except requests.exceptions.RequestException as e:
        print("Failed - create_conversions_for_each_campaign_dataset()")
        print(e)
        send_email("brianshaller@gmail.com", "Failed - create_conversions_for_each_campaign_dataset() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

