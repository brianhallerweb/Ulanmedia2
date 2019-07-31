from config.config import *
from config.mgid_token import mgid_token
from datetime import datetime, timedelta
import pytz
import sys
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token 
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token 
from functions.data_acquisition_functions.create_p_and_c_widgets_for_one_campaign_dataset import create_p_and_c_widgets_for_one_campaign_dataset
from functions.misc.get_campaign_sets import get_campaign_sets 

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

campaigns = get_campaign_sets()
    
for campaign in campaigns:
    # In this script, vol_id is only used for the output file name
    vol_id = campaign["vol_id"]
    # if vol_id == "c19b4d98-4be5-446b-ae0c-91649ad0010b":
        # create_p_and_c_widgets_for_one_campaign_dataset(mgid_token, vol_token,
                # campaign, 180, f"{vol_id}_oneeighty_p_and_c_widgets_for_one_campaign_dataset")


    # yesterday
    days_ago = 1
    create_p_and_c_widgets_for_one_campaign_dataset(mgid_token, vol_token,
            campaign, days_ago,
            f"{vol_id}_yesterday_p_and_c_widgets_for_one_campaign_dataset")

    # last 7 days
    days_ago = 7
    create_p_and_c_widgets_for_one_campaign_dataset(mgid_token, vol_token,
            campaign, days_ago, f"{vol_id}_seven_p_and_c_widgets_for_one_campaign_dataset")

    # last 30 days
    days_ago = 30
    create_p_and_c_widgets_for_one_campaign_dataset(mgid_token, vol_token,
            campaign, days_ago, f"{vol_id}_thirty_p_and_c_widgets_for_one_campaign_dataset")

    # last 90 days
    days_ago = 90

    create_p_and_c_widgets_for_one_campaign_dataset(mgid_token, vol_token,
            campaign, days_ago, f"{vol_id}_ninety_p_and_c_widgets_for_one_campaign_dataset")

    # last 180 days
    days_ago = 180 
    create_p_and_c_widgets_for_one_campaign_dataset(mgid_token, vol_token,
            campaign, days_ago, f"{vol_id}_oneeighty_p_and_c_widgets_for_one_campaign_dataset")
