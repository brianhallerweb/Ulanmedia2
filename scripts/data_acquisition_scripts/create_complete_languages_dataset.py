from config.config import *
from functions.data_acquisition_functions.create_complete_languages_dataset import create_complete_languages_dataset
import sys

#############################################
date_range = "yesterday"

create_complete_languages_dataset(date_range)

print(f"{date_range} languages dataset created")

###########################################
date_range = "seven"

create_complete_languages_dataset(date_range)

print(f"{date_range} languages dataset created")

#############################################
date_range = "thirty"

create_complete_languages_dataset(date_range)

print(f"{date_range} languages dataset created")

#############################################
date_range = "ninety"

create_complete_languages_dataset(date_range)

print(f"{date_range} languages dataset created")

#############################################
date_range = "oneeighty"

create_complete_languages_dataset(date_range)

print(f"{date_range} languages dataset created")
#############################################


