from functions.misc.send_email import send_email
from datetime import datetime
import requests
import json
import sys

def set_vol_campaign_cost(token, campaign_id, start_date, end_date, cost):
    if cost <= 0:
        return print("cost <= 0 so didn't update")
    try:
        res = requests.post("https://api.voluum.com/report/manual-cost", 
            headers ={"Content-type": "application/json",
                "Accept": "application/json",
                "cwauth-token": token}, 
            data = json.dumps({"from": start_date, "to": end_date,
                "timeZone": "America/Los_Angeles", 
                "campaignId": campaign_id, 
                "cost": cost}))
        if res.status_code == 500:
            return 500
        if res.status_code == 417:
            if res.json()["error"]["code"] == "NO_VISITS_PERIOD":
                return print("no visits so didn't update")
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        send_email("brianshaller@gmail.com", "Failed - set_vol_campaign_cost() at " +
                str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()


