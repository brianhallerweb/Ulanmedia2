from functions.data_acquisition_functions.create_offers_for_each_flow_rule_dataset import create_offers_for_each_flow_rule_dataset

#############################################
# create a data set for yesterday 
date_range = "yesterday"

create_offers_for_each_flow_rule_dataset(date_range)

print(f"{date_range} offers for each flow rule dataset created")

#############################################
# create a data set for the last 7 days
date_range = "seven"

create_offers_for_each_flow_rule_dataset(date_range)

print(f"{date_range} offers for each flow rule dataset created")

#############################################
# create a data set for the last 30 days
date_range = "thirty"

create_offers_for_each_flow_rule_dataset(date_range)

print(f"{date_range} offers for each flow rule dataset created")

#############################################
# create a data set for the last 90 days
date_range = "ninety"

create_offers_for_each_flow_rule_dataset(date_range)

print(f"{date_range} offers for each flow rule dataset created")

############################################
# create a data set for the last 180 days
date_range = "oneeighty"

create_offers_for_each_flow_rule_dataset(date_range)

print(f"{date_range} offers for each flow rule dataset created")

