from config.config import *
from functions.data_acquisition_functions.create_gprs_for_each_p_offer_dataset import create_gprs_for_each_p_offer_dataset
import sys

date_range = sys.argv[1]
# date_range = "oneeighty"

print(create_gprs_for_each_p_offer_dataset(date_range))


