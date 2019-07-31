from config.config import *
from functions.data_acquisition_functions.create_countries_dataset import create_countries_dataset
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.misc.create_vol_date_range import create_vol_date_range

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

#############################################
# create a data set for yesterday 
date_range = "yesterday"
vol_dates = create_vol_date_range(1, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

create_countries_dataset(vol_token, vol_start_date, vol_end_date, date_range)

print(f"{date_range} countries dataset created")

#############################################
# create a data set for the last seven days
date_range = "seven"
vol_dates = create_vol_date_range(7, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

create_countries_dataset(vol_token, vol_start_date, vol_end_date, date_range)

print(f"{date_range} countries dataset created")

#############################################
# create a data set for the last thirty days
date_range = "thirty"
vol_dates = create_vol_date_range(30, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

create_countries_dataset(vol_token, vol_start_date, vol_end_date, date_range)

print(f"{date_range} countries dataset created")

#############################################
# create a data set for the last ninety days
date_range = "ninety"
vol_dates = create_vol_date_range(90, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

create_countries_dataset(vol_token, vol_start_date, vol_end_date, date_range)

print(f"{date_range} countries dataset created")

#############################################
# create a data set for the last ninety days
date_range = "oneeighty"
vol_dates = create_vol_date_range(180, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

create_countries_dataset(vol_token, vol_start_date, vol_end_date, date_range)

print(f"{date_range} countries dataset created")


