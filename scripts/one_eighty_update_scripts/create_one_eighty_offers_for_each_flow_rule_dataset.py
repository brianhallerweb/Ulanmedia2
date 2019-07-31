from functions.data_acquisition_functions.create_offers_for_each_flow_rule_dataset import create_offers_for_each_flow_rule_dataset

############################################
# create a data set for the last 180 days
date_range = "oneeighty"

create_offers_for_each_flow_rule_dataset(date_range)

print(f"{date_range} offers for each flow rule dataset created")


