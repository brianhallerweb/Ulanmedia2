from config.config import *
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.misc.create_mgid_date_range import create_mgid_date_range
from functions.data_acquisition_functions.get_mgid_widget_clicks_and_costs_by_campaign import get_mgid_widget_clicks_and_costs_by_campaign
from functions.data_acquisition_functions.get_vol_widget_conversions_by_campaign import get_vol_widget_conversions_by_campaign
from datetime import datetime, timedelta
import json
import sys
import re
import os

def create_p_and_c_widgets_for_one_campaign_dataset(mgid_token, vol_token,
        campaign, days_ago, output_name):

    # create mgid and vol dates
    vol_dates = create_vol_date_range(days_ago, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    mgid_dates = create_mgid_date_range(days_ago, mgid_timezone)
    mgid_start_date = mgid_dates[0]
    mgid_end_date = mgid_dates[1]

    # extract needed campaign info from mgid and vol
    name = campaign["name"]
    mgid_id = campaign["mgid_id"]
    vol_id = campaign["vol_id"]
    mpl = campaign["max_lead_cpa"] 
    mps = campaign["max_sale_cpa"] 
    mpc_pattern = re.compile(r'.*cpc_(.*)')
    res = mpc_pattern.findall(campaign["name"])
    c_bid = float(list(res)[0])

    # create a metadata dictionary
    metadata = {"mgid_start_date": mgid_start_date,
            "mgid_end_date": mgid_end_date,
            "vol_start_date": vol_start_date,
            "vol_end_date": vol_end_date,
            "name": name,
            "mgid_id": mgid_id,
            "vol_id": vol_id,
            "mpl": mpl,
            "mps": mps, 
            "c_bid": c_bid 
             }

    # get clicks and costs for each widget from mgid
    mgid_widget_data = get_mgid_widget_clicks_and_costs_by_campaign(mgid_token,
            mgid_id, mgid_start_date,
            mgid_end_date)

    # get conversion data for each widget from vol
    vol_results = get_vol_widget_conversions_by_campaign(vol_token,
            vol_id, vol_start_date,
            vol_end_date)
    
    # merge the data from mgid and voluum into one dictionary
    for widget_id in mgid_widget_data:

        if widget_id not in vol_results:
            mgid_widget_data[widget_id]['revenue'] = 0.0 
            mgid_widget_data[widget_id]['leads'] = 0 
            mgid_widget_data[widget_id]['sales'] = 0 
            mgid_widget_data[widget_id]['referrer'] = [] 
        else:
            vol_widget = vol_results[widget_id]
            for key in vol_widget:
                mgid_widget_data[widget_id][key] = vol_widget[key]

    complete_widget_data = mgid_widget_data

    complete_data_ready_for_json = {"metadata": metadata,
            "data": complete_widget_data}

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/p_and_c_widgets_for_one_campaign/{output_name}.json", "w") as file:
        json.dump(complete_data_ready_for_json, file)

    print(f"{output_name} created")

