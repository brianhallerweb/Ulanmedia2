from config.config import *
from datetime import datetime, timedelta
import pytz

def create_vol_date_range(days_ago, timezone):
    start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago)
    start_date_pst = start_date_utc.astimezone(pytz.timezone(timezone))
    end_date_utc = pytz.utc.localize(datetime.utcnow()) 
    end_date_pst = end_date_utc.astimezone(pytz.timezone(timezone))
    return [start_date_pst.strftime("%Y-%m-%d"),
            end_date_pst.strftime("%Y-%m-%d")]

