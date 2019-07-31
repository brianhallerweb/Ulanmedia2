from functions.misc.send_email import send_email
from datetime import datetime
import sys
import os
import json


def get_campaign_sets():
    with open(f'{os.environ.get("ULANMEDIAAPP")}/campaign_sets/campaign_sets.json', 'r') as file:
        campaign_sets = json.load(file)
    return campaign_sets

