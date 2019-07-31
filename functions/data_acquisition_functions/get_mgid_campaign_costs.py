from functions.misc.send_email import send_email
from functions.misc.get_and_return_new_mgid_token import get_and_return_new_mgid_token
from datetime import datetime
import sys
import requests

def get_mgid_campaign_costs(token, client_id, start, end):
    try:
        res = requests.get(
        f"https://api.mgid.com/v1/goodhits/clients/{client_id}/campaigns-stat?token={token}&dateInterval=interval&startDate={start}&endDate={end}")
        if res.status_code == 401:
            mgid_token = get_and_return_new_mgid_token()
            return get_mgid_campaign_costs(mgid_token, client_id, start, end)

        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print("Failed - get_mgid_campaign_costs")
        send_email("brianshaller@gmail.com", "Failed -                get_mgid_campaign_costs() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()
