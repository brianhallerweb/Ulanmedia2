from config.config import *
from functions.data_acquisition_functions.create_conversions_for_each_campaign_dataset import create_conversions_for_each_campaign_dataset
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.misc.create_vol_date_range import create_vol_date_range

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

date_range = "oneeighty"
vol_dates = create_vol_date_range(180, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

create_conversions_for_each_campaign_dataset(vol_token, vol_start_date, vol_end_date, date_range)

print(f"{date_range} conversions for each campaign dataset created")


