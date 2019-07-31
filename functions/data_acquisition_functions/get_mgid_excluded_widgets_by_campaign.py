from functions.misc.send_email import send_email
from functions.misc.get_and_return_new_mgid_token import get_and_return_new_mgid_token
from datetime import datetime
import requests
import sys

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id, mgid_campaign_id):
    url=f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/campaigns/{mgid_campaign_id}?token={mgid_token}";
    try:
        response = requests.get(url)
        if response.status_code == 401:
            new_mgid_token = get_and_return_new_mgid_token()
            return get_mgid_excluded_widgets_by_campaign(new_mgid_token, mgid_client_id, mgid_campaign_id)

        response.raise_for_status()
        response = response.json()
        # the response is a dictionary of lists. The keys are widget ids.
        # The values are sources. If a widget id has a source, it must be 
        # this concatenation is necessary {widget_id}s{source_id}.
        # One strange thing about the response is that the source id appears
        # to be in a list but the [] are actually just part of the source id
        # string.
        excluded_widgets = []
        for key, value in response["widgetsFilterUid"]["widgets"].items():
            if (value == "[]") | (value == None):
                excluded_widgets.append(key)
            else:
                value = value.replace("[", "")
                value = value.replace("]", "")
                value = value.replace(",", "")
                c_widgets = value.split(" ")
                for c_widget in c_widgets:
                    excluded_widgets.append(f"{key}s{c_widget}")
        # excluded_widgets is a list of excluded widget ids
        return excluded_widgets
    except requests.exceptions.RequestException as e:
        print("Failed - get_mgid_excluded_widgets_by_campaign")
        send_email("brianshaller@gmail.com", "Failed - get_mgid_excluded_widgets_by_campaign() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

# explore what this function returns
# from config.config import *
# from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token

# mgid_token = get_mgid_access_token(mgid_login, mgid_password)
# data = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id, "527385")
# print(data)

