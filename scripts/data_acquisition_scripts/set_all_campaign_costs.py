from datetime import datetime, timedelta
import pytz
from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.set_vol_campaign_cost import set_vol_campaign_cost
from functions.data_acquisition_functions.get_all_campaign_revenues_by_traffic_source import get_all_campaign_revenues_by_traffic_source
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_mgid_campaign_costs import get_mgid_campaign_costs
from functions.misc.create_mgid_date_range import create_mgid_date_range
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets 
from functions.misc.send_email import send_email
import sys

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

vol_dates = create_vol_date_range(1, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]
mgid_dates = create_mgid_date_range(1, mgid_timezone)
mgid_start_date = mgid_dates[0]
mgid_end_date = mgid_dates[1]

# get cost by campaign from mgid
mgid_campaign_costs = get_mgid_campaign_costs(mgid_token, mgid_client_id,
                                              mgid_start_date, mgid_end_date)

# get a new version of the campaign_sets text file 
campaign_sets = get_campaign_sets() 

# update voluum's records on cost per campaign
# also, add up the total cost of all campaigns
total_campaign_cost = 0
for row in campaign_sets:
    mgid_campaign_id = str(row["mgid_id"])
    vol_campaign_id = str(row["vol_id"])
    mgid_campaign_cost = mgid_campaign_costs["campaigns-stat"][mgid_campaign_id]["spent"]

    # 3/9/19 set_vol_campaign_cost() started to fail in what seemed to be a
    # random way
    attempt_number = 0
    while attempt_number < 10:
        status = set_vol_campaign_cost(vol_token, vol_campaign_id,
                          vol_start_date, vol_end_date, mgid_campaign_cost)
        if status == 500:
            attempt_number += 1
        else:
            break
    if attempt_number == 10:
        error_message = "Failed - set_vol_campaign_cost() failed 10 times in a row"
        print(error_message)
        send_email("brianshaller@gmail.com", error_message, error_message)
        sys.exit()

        
    total_campaign_cost += mgid_campaign_cost

# get revenue by campaign from voluum 
revenues = get_all_campaign_revenues_by_traffic_source(vol_token,
                                                       mgidVolTrafficSourceId 
                                                       , vol_start_date, vol_end_date)

# Calculate total revenue
total_revenue = 0
for campaign_revenue in revenues["rows"]:
    total_revenue += campaign_revenue["revenue"]


total_revenue_rounded = round(total_revenue, 2)
total_campaign_cost_rounded = round(total_campaign_cost, 2)
total_profit_rounded = round(total_revenue - total_campaign_cost, 2)

# Send an email with yesterdays totals for  visits, cost, and revenue. 
subject = f"{mgid_start_date} ---- total revenue = {total_revenue_rounded}, total cost = {total_campaign_cost_rounded}, total profit= {total_profit_rounded}."
message = f"{mgid_start_date}\ntotal revenue = {total_revenue_rounded}\ntotal cost = {total_campaign_cost_rounded}\ntotal profit = {total_profit_rounded}."
send_email("brianshaller@gmail.com", subject, message)
send_email("mikeseo@gmail.com", subject, message)
