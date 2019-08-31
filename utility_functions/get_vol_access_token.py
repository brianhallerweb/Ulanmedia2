from utility_functions.send_email import send_email
from datetime import datetime
import requests
import json
import sys

def get_vol_access_token(id, key):
    try:
        res = requests.post("https://api.voluum.com/auth/access/session",
                headers = {"Content-type": "application/json",
                    "Accept": "application/json"},
                data = json.dumps({"accessId": id, "accessKey": key}))
        res.raise_for_status()
        return res.json()["token"]
    except requests.exceptions.RequestException as e:
        print("Failed - get_vol_access_token()") 
        send_email("brianshaller@gmail.com", "Failed - get_vol_access_token() at " +
                str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()
