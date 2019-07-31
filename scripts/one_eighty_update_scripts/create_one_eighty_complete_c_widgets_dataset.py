from config.config import *
from datetime import datetime, timedelta
import sys
import json
from functions.data_acquisition_functions.create_complete_c_widgets_dataset import create_complete_c_widgets_dataset


date_range = "oneeighty"

create_complete_c_widgets_dataset(date_range, f"{date_range}_complete_c_widgets_dataset")

print(f"{date_range} complete c widgets dataset created")

