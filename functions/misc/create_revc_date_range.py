from config.config import *
from datetime import datetime, timedelta
import pytz

def create_revc_date_range(days_ago, timezone):
    start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago)
    start_date_pst = start_date_utc.astimezone(pytz.timezone(timezone))
    # for mgid, the end date is inclusive, so the end date needs to be
    # yesterday in order to include yesterdays data. 
    end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(1)
    end_date_pst = end_date_utc.astimezone(pytz.timezone(timezone))
    return [start_date_pst.strftime("%Y-%m-%d"),
            end_date_pst.strftime("%Y-%m-%d")]


print(create_revc_date_range(7, revc_timezone))
