from config.config import *
from functions.misc.send_email import send_email
from datetime import datetime
import requests
import sys

def get_vol_daily_stats_data(token, start_date, end_date, timezone):
    vol_url = f"https://api.voluum.com/report?from={start_date}T00%3A00%3A00Z&to={end_date}T00:00:00Z&tz={timezone}&sort=campaignName&direction=desc&columns=campaignName&columns=day&columns=campaignId&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=cpv&groupBy=campaign&groupBy=day&offset=0&limit=1000000&include=ACTIVE&conversionTimeMode=VISIT&filter1=traffic-source&filter1Value={mgidVolTrafficSourceId}";
    try: 
        res = requests.get(vol_url, headers = {"cwauth-token":
            token})
        res.raise_for_status()
        vol_response = res.json()
        if vol_response["totalRows"] != len(vol_response["rows"]):
            send_email("brianshaller@gmail.com", "Failed - get_vol_daily_stats_data at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), "all data not returned from voluum")
            raise Exception("voluum didn't return all the conversion data")
        return vol_response["rows"]

    except requests.exceptions.RequestException as e:
        print("exception handled")
        send_email("brianshaller@gmail.com", "Failed - get_vol_daily_stats_data at " +
        str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()
