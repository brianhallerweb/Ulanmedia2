from config.config import *
from datetime import datetime, timedelta
import sys
import json
from functions.data_acquisition_functions.create_complete_c_widgets_dataset import create_complete_c_widgets_dataset

#################################

date_range = "yesterday"

create_complete_c_widgets_dataset(date_range, f"{date_range}_complete_c_widgets_dataset")

print(f"{date_range} complete c widgets dataset created")

#################################

date_range = "seven"

create_complete_c_widgets_dataset(date_range, f"{date_range}_complete_c_widgets_dataset")

print(f"{date_range} complete c widgets dataset created")

#################################

date_range = "thirty"

create_complete_c_widgets_dataset(date_range, f"{date_range}_complete_c_widgets_dataset")

print(f"{date_range} complete c widgets dataset created")

#################################

date_range = "ninety"

create_complete_c_widgets_dataset(date_range, f"{date_range}_complete_c_widgets_dataset")

print(f"{date_range} complete c widgets dataset created")

#################################

date_range = "oneeighty"

create_complete_c_widgets_dataset(date_range, f"{date_range}_complete_c_widgets_dataset")

print(f"{date_range} complete c widgets dataset created")

################################

print("all complete_c_widgets_datasets created")
