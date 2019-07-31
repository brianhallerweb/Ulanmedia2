from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets
from datetime import datetime
import requests
import sys
import json
import os

def create_languages_dataset(token, start_date, end_date, date_range):
    try:
        url = f"https://api.voluum.com/report?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&conversionTimeMode=VISIT&sort=campaignName&direction=asc&columns=campaignName&columns=languageName&columns=campaignId&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&columns=cpa&groupBy=campaign&groupBy=language&offset=0&limit=100000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"
        res = requests.get(url, headers = {"cwauth-token":
                token})
        res.raise_for_status()
        res = res.json()

        languages = {"metadata": {"vol_start_date": start_date,
                                 "vol_end_date": end_date
                                 },
                    "data": {}}

        campaigns = get_campaign_sets()
        vol_ids = [] 
        for campaign in campaigns:
            vol_ids.append(campaign["vol_id"])

        for row in res["rows"]:
            language_name = row["languageName"]
            if language_name == "Spanish/Castilian":
                language_name = language_name.replace("/", ", ")
            campaign_id = row["campaignId"]
            if campaign_id not in vol_ids:
                continue
            if language_name not in languages["data"]:
                languages["data"][language_name] = {campaign_id: {
                    "campaign_id": campaign_id,
                    "language_name": language_name,
                    "clicks": row["visits"],
                    "conversions": row["conversions"],
                    "cost": row["cost"],
                    "profit": row["profit"],
                    "revenue": row["revenue"]
                    }}
            else:
                languages["data"][language_name][campaign_id] = {
                    "campaign_id": campaign_id,
                    "language_name": language_name,
                    "clicks": row["visits"],
                    "conversions": row["conversions"],
                    "cost": row["cost"],
                    "profit": row["profit"],
                    "revenue": row["revenue"]
                    }

        with open(f"{os.environ.get('ULANMEDIAAPP')}/data/languages/{date_range}_languages_dataset.json", "w") as file:
            json.dump(languages, file)

    except requests.exceptions.RequestException as e:
            print("Failed - create_languages_dataset()")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - create_languages_dataset() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()
            

