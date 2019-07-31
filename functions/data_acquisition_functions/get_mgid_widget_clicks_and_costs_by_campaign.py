from functions.misc.send_email import send_email
from functions.misc.get_and_return_new_mgid_token import get_and_return_new_mgid_token
from datetime import datetime
import requests 
import sys

import pprint
pp=pprint.PrettyPrinter(indent=2)

def get_mgid_widget_clicks_and_costs_by_campaign(token, campaign_id, start_date, end_date):
    try:
        url =f"https://api.mgid.com/v1/goodhits/campaigns/{campaign_id}/quality-analysis?token={token}&campaignId={campaign_id}&dateInterval=interval&startDate={start_date}&endDate={end_date}";
        response = requests.get(url) 
        if response.status_code == 401:
            mgid_token = get_and_return_new_mgid_token()
            return get_mgid_widget_clicks_and_costs_by_campaign(mgid_token, campaign_id, start_date, end_date)

        response.raise_for_status()
        response = response.json()
        # The logic below esstenially loops through each each widget and records
        # clicks into my dictionary of widgets. The only complication is if a widget
        # has sources, which are like child widgets. Sources are kept in a list.
        # For each source, if it is "0", that means it is really the parent widget,
        # and its data will be stored in voluum as such. If the source is not "0",
        # then it really is a child widget and its data is stored in voluum as
        # parent widget id + s + child widget id. 
        # The reason why it matters how it is stored in voluum is because the
        # purpose of this function is to contribute to getting accurate widget
        # data. Mgid provides accurate data on clicks and cost and voluum provides
        # accurate data on the rest (conversions, revenue, etc).
        widgets_data = {}
        if response[campaign_id][start_date + "_" + end_date] == []:
            return widgets_data
        for id, data in response[campaign_id][start_date + "_" + end_date].items():
            widget_id = id
            if data["sources"]:
                for source_id, source_data in data["sources"].items():
                    if source_id is not "0":
                        widget_id = f"{id}s{source_id}"
                    widgets_data[widget_id] = {"widget_id": widget_id, "clicks":
                    source_data["clicks"], "cost": source_data["spent"],
                    "coeff": source_data["qualityFactor"]}
            else: 
                widgets_data[widget_id] = {"widget_id": widget_id, "clicks":
                        data["clicks"], "cost": data["spent"],
                        "coeff": data["qualityFactor"]}

        return widgets_data 
    except requests.exceptions.RequestException as e:
        print("Failed - get_mgid_widget_clicks_and_costs_by_campaign")
        send_email("brianshaller@gmail.com", "Failed - get_mgid_widget_clicks_and_costs_by_campaign() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

