from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.create_days_for_one_campaign_dataset import create_days_for_one_campaign_dataset

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

create_days_for_one_campaign_dataset(vol_token, mgid_token,
        50 ,"days_for_one_campaign_dataset")


