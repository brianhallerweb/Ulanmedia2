import requests 
from datetime import datetime, timedelta
import pytz
import sys
import mysql.connector
import re
from ulanmedia2_config.config import * 
from utility_functions.create_complete_campaign_sets import create_complete_campaign_sets
from utility_functions.get_vol_access_token import get_vol_access_token
from get_vol_id_from_mgid_id import get_vol_id_from_mgid_id
from get_campaign_name_from_mgid_id import get_campaign_name_from_mgid_id

import pprint
pp=pprint.PrettyPrinter(indent=2)

def update_traffic_click_id_in_conversions_table(days_ago):
    if (days_ago != 1):
        print("improper use of update_traffic_click_id_in_conversions_table()")
        sys.exit()
    
    ###########
    token = get_vol_access_token(vol_access_id, vol_access_key)

    #############
    # vol dates
    
    timezone = 'america/los_angeles'
    start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago)
    start_date_pst = start_date_utc.astimezone(pytz.timezone(timezone))
    end_date_utc = pytz.utc.localize(datetime.utcnow()) 
    end_date_pst = end_date_utc.astimezone(pytz.timezone(timezone))
    start_date = start_date_pst.strftime("%Y-%m-%d")
    end_date = end_date_pst.strftime("%Y-%m-%d")

    date_to_put_in_sql = start_date_pst.replace(tzinfo=None, microsecond=0)

    ##################
    # set up mysql

    mydb = mysql.connector.connect(
      host="localhost",
      user= mysql_user,
      passwd= mysql_password,
      database="ulanmedia"
    )

    mycursor = mydb.cursor()

    # sql = f"delete from cost_ads where cost_date like '{start_date}%'"

    # mycursor.execute(sql)
    ####################

    url = f"https://api.voluum.com/report/conversions?from={start_date}T00%3A00%3A00Z&to={end_date}T00%3A00%3A00Z&tz=America%2FLos_Angeles&sort=postbackTimestamp&direction=desc&columns=postbackTimestamp&columns=externalId&columns=clickId&columns=transactionId&columns=revenue&groupBy=conversion&offset=0&limit=100000&include=ACTIVE"
    res = requests.get(url, headers = {"cwauth-token": token})
    res = res.json()
    for row in res["rows"]:
        vol_click_id = row["clickId"]
        mgid_click_id = row["externalId"]
        sql = f"UPDATE `conversions` SET `traffic_click_id` = '{mgid_click_id}' WHERE `voluum_click_id` = '{vol_click_id}'"

        mycursor.execute(sql)

        mydb.commit()



