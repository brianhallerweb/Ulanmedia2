from functions.misc.send_email import send_email
from datetime import datetime
import sys
import requests
import json
import os

import pandas as pd
from pandas.compat import StringIO

def update_campaign_sets_file():
    try:
        res = requests.get("https://www.ulanmedia.com/mgid/campaign_sets.txt")
        res.raise_for_status()
        campaign_sets_data = StringIO("vol_id\tmgid_id\tname\tmax_lead_cpa\tmax_sale_cpa\n" +
                str(res.text))
        campaign_sets_data = pd.read_csv(campaign_sets_data, sep="\t").to_dict("records")
        for campaign in campaign_sets_data:
            campaign["mgid_id"] = str(campaign["mgid_id"])
        # campaign_sets_data is a list of dictionaries. Each dictionary is
        # campaign that looks like this:
        #  { 'max_lead_cpa': 15,
        #    'max_sale_cpa': 300,
        #    'mgid_id': '517506',
        #    'name': 'bin_world-wide-t2_swedish_mobile_cpc_0.04',
        #    'vol_id': 'e6f4ac2b-ccec-4606-bd1a-9084088c4df0'}
        with open(f"{os.environ.get('ULANMEDIAAPP')}/campaign_sets/campaign_sets.json", "w") as file:
           json.dump(campaign_sets_data, file)
    except requests.exceptions.RequestException as e:
            print("Failed to update campaign sets file")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - update_campaign_sets_file() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()

