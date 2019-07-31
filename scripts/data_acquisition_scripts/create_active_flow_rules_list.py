from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.create_active_flow_rules_list import create_active_flow_rules_list

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

create_active_flow_rules_list(vol_token)

print("active flow rules list created")

