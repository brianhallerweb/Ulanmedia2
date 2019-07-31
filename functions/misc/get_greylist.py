from functions.misc.send_email import send_email
from datetime import datetime
import requests
import sys

def get_greylist():
    try:
        res = requests.get("https://ulanmedia.brianhaller.net/api/readgreylist")
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
            print("Failed to update campaign sets")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - update_campaign_sets() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()

