from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.get_all_campaign_conversions_by_traffic_source import get_all_campaign_conversions_by_traffic_source
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_mgid_campaign_costs import get_mgid_campaign_costs
from functions.data_acquisition_functions.create_campaigns_for_all_campaigns_dataset import create_campaigns_for_all_campaigns_dataset
from functions.misc.send_email import send_email

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

#############################################
# create a data set for yesterday 
days_ago = 1

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago,
        "yesterday_campaigns_for_all_campaigns_dataset")

#############################################
# create a data set for 7 days 
days_ago = 7

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago,
        "seven_campaigns_for_all_campaigns_dataset")

#############################################
# create a data set for 30 days 
days_ago = 30

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago,
        "thirty_campaigns_for_all_campaigns_dataset")

#############################################
# create a data set for 90 days 
days_ago = 90

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago,
        "ninety_campaigns_for_all_campaigns_dataset")

#############################################
# create a data set for 180 days 
days_ago = 180

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago,
        "oneeighty_campaigns_for_all_campaigns_dataset")





