from config.config import *
from functions.misc.send_email import send_email
from datetime import datetime
import requests
import re
import sys
import json

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def create_active_flow_rules_list(token):
    try:
        flow_id = "da8f9291-462d-43e7-98a4-24d62f608297"
        url = f"https://api.voluum.com/flow/{flow_id}"
        response = requests.get(url, headers = {"cwauth-token": token})
        response.raise_for_status()
        response = response.json()

        active_flow_rules = []
        for offer in response["defaultPaths"]:
            active_flow_rules.append(offer["name"])
        for offer in response["conditionalPathsGroups"]:
            active_flow_rules.append(offer["name"])
            
        with open(f"../../data/active_flow_rules/active_flow_rules.json", "w") as file:
            json.dump(active_flow_rules, file)

    except requests.exceptions.RequestException as e:
        print("Failed - create_active_flow_rules_list")
        send_email("brianshaller@gmail.com", "Failed - create_active_flow_rules_list() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

