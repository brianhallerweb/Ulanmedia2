from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.create_campaigns_for_all_campaigns_dataset import create_campaigns_for_all_campaigns_dataset

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

days_ago = 180

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago,
        "oneeighty_campaigns_for_all_campaigns_dataset")





