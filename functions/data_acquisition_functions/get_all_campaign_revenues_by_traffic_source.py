from config.config import *
from datetime import datetime
import requests
import sys
from functions.misc.send_email import send_email

def get_all_campaign_revenues_by_traffic_source(token, traffic_source_id,
        start_date, end_date):
    url=f"https://api.voluum.com/report?from={start_date}T00%3A00%3A00Z&to={end_date}T00%3A00%3A00Z&tz={mgid_timezone}&sort=visits&direction=desc&columns=campaignName&columns=campaignId&columns=visits&columns=revenue&groupBy=campaign&offset=0&limit=100000&include=ACTIVE&conversionTimeMode=VISIT&filter1=traffic-source&filter1Value={traffic_source_id}";
    try:
        res = requests.get(url, headers = {"cwauth-token": token})
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print("Failed - get_all_campaign_revenues_by_traffic_source()") 
        send_email("brianshaller@gmail.com", "Failed - get_all_campaign_revenues_by_traffic_source at " +
                str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

