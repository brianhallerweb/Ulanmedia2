from config.config import *
from config.mgid_token import mgid_token
from functions.misc.get_and_return_new_mgid_token import get_and_return_new_mgid_token
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
import requests
import sys

def get_mgid_included_widgets_by_campaign(token, campaign_id, start_date, end_date):
    url =f"https://api.mgid.com/v1/goodhits/campaigns/{campaign_id}/quality-analysis?token={token}&campaignId={campaign_id}&dateInterval=interval&startDate={start_date}&endDate={end_date}";
    response = requests.get(url) 
    if response.status_code == 401:
        mgid_token = get_and_return_new_mgid_token()
        return get_mgid_included_widgets_by_campaign(mgid_token, campaign_id, start_date, end_date)

    response.raise_for_status()
    response = response.json()

    widgets = []
    if response[campaign_id][start_date + "_" + end_date] == []:
        return widgets
    for id, data in response[campaign_id][start_date + "_" + end_date].items():
        widget_id = id
        widgets.append(widget_id)
        if data["sources"]:
            for source_id, source_data in data["sources"].items():
                if source_id is not "0":
                    widget_id = f"{id}s{source_id}"
                    widgets.append(widget_id)

    excluded_widgets = get_mgid_excluded_widgets_by_campaign(token, mgid_client_id, campaign_id)
    included_widgets = []
    for widget in widgets:
        if widget not in excluded_widgets:
            included_widgets.append(widget)

    return included_widgets

# problem solving from 5/28/19
# from functions.misc.create_mgid_date_range import create_mgid_date_range
# dates = create_mgid_date_range(80, mgid_timezone)
# start = dates[0]
# print(start)
# end = dates[1]

# # for campaign 506299, the widget is included 80 or more days ago, and not included 79
# # or less

# widgets = get_mgid_included_widgets_by_campaign(mgid_token, "506299", start, end)

# if "5722923" in widgets:
    # print("yes")
# else:
    # print("no")

